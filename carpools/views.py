from django.shortcuts import render
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Carpool, CompletedCarpool, Caution
from django.views import View
from .serializers import CarpoolSerializer, CarpoolDetailSerializer

import datetime

# 매일 자정마다 2일이 지난 카풀의 end_carpool field 값을 True로 초기화합니다.
def blockCarpool():
    now = datetime.datetime.now()
    carpools = Carpool.objects.all()
    for carpool in carpools:
        diff = now - carpool.created_at
        if diff.days >= 2:
            carpool.end_carpool = True
            carpool.save()
    return

# 매일 자정마다 30일이 지난 완료된 카풀을 db에서 삭제합니다.
def deleteCompletedCarpool():
    now = datetime.datetime.now()
    completedcarpools = CompletedCarpool.objects.all()
    for completedcarpool in completedcarpools:
        diff = now - completedcarpool.created_at
        if diff.days >= 30:
            completedcarpool.delete()
    return

# 아래에 여러분의 기능을 구현해주세요...화이팅!

#48시간 지난 카풀은 제외하고 보여주기
class CarpoolListView(APIView):
    def get_queryset(self):
        now = timezone.now()
        
        Carpool.objects.filter(created_at__lt=now - datetime.timedelta(days=2)).update(end_carpool=True)
        return Carpool.objects.filter(end_carpool=False)
    
    def get(self, request):
        #end_carpool이 False인 카풀만 조회
        active_carpools = self.get_queryset()
        serializer = CarpoolSerializer(active_carpools, many=True)
        #many=True 는 serialize 시 여러 객체 처리할 것을 나타냅니다.
        #get_queryset 메서드가 여러 Carpool객체를 반환하기 때문에 ->객체 목록을 serialize 가능
        return Response(serializer.data)


#목록 전체 보기

@api_view(['GET'])
def carpool_list(request):
    carpools = Carpool.objects.all()
    serializer = CarpoolSerializer(carpools, many = True)
    return Response({"carpools": serializer.data})

#카풀 상세 보기

@api_view(['GET'])
def carpool_detail(request, pk):
    try:
        carpool = Carpool.objects.get(pk = pk)
    except Carpool.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CarpoolDetailSerializer(carpool)
    return Response(serializer.data)
