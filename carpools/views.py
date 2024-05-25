from django.shortcuts import render, get_object_or_404
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
    def get(self, request):
        now = timezone.now()
        #end_carpool이 False인 카풀만 조회
        active_carpools = Carpool.objects.filter(end_carpool=False)
        serializer = CarpoolSerializer(active_carpools, many=True)
        return Response(serializer.data)
    

#카풀 상세 보기

@api_view(['GET'])
def carpool_detail(request, pk):
    carpool = get_object_or_404(Carpool, pk=pk)
    serializer = CarpoolDetailSerializer(carpool)
    return Response(serializer.data)