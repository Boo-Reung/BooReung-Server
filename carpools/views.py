from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Carpool, CompletedCarpool, Caution

from .serializers import *


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
        #carpool_date가 현재 날짜보다 이후인 카풀만 필터링
        active_carpools = Carpool.objects.filter(carpool_date__gt=now)
        serializer = CarpoolListSerializer(active_carpools, many=True)
        return Response(serializer.data)
    

#카풀 상세 보기

@api_view(['GET'])
def carpool_detail(request, pk):
    carpool = get_object_or_404(Carpool, pk=pk)
    serializer = CarpoolDetailSerializer(carpool)
    return Response(serializer.data)

#프론트에서 json 형태로 정보를 받은 후 그 데이터들을 db에 저장하는 기능

#카풀 주최하기
class PostAPIView(APIView):
    def post(self, request):
        serializer=CarpoolCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "carpool created successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "carpool created failed"}, status=status.HTTP_400_BAD_REQUEST)
        
#성사된 카풀 정보 입력
class CompletedAPIView(APIView):
    def post(self, request):
        serializer=InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "completed carpool info created success"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "completed carpool info created failed"}, status=status.HTTP_400_BAD_REQUEST)
# 로딩창 주의사항을 랜덤으로 띄웁니다.
import random

class RandomCautionView(APIView):
    def get(self, request):
        count = Caution.objects.count()
        if count == 0:
            return Response({"message": "No cautions available."}, status=404)
        random_idx = random.randint(0, count - 1)
        caution = Caution.objects.all()[random_idx]
        serializer = CautionSerializer(caution)
        return Response(serializer.data)
    
# 카풀 목록 필터링(목적, 성별, 경로, 인워느 가격, 날짜) 기능입니다.
@api_view(['POST'])
def filter_carpools(request):
    filters = request.data

    carpools = Carpool.objects.all()

    if filters.get('type'):
        carpools = carpools.filter(type=filters['type'])

        if filters['type'] == '통학':
            if filters.get('dept'):
                carpools = carpools.filter(dept=filters['dept'])
            if filters.get('dest'):
                carpools = carpools.filter(dest=filters['dest'])
        elif filters['type'] == '여행':
            if filters.get('dept'):
                carpools = carpools.filter(dept__contains=filters['dept'])
            if filters.get('dest'):
                carpools = carpools.filter(dest__contains=filters['dest'])

    # 나머지 필터링 조건 적용
    if filters.get('client_gender'):
        carpools = carpools.filter(client_gender=filters['client_gender'])
    if filters.get('min_member'):
        carpools = carpools.filter(member__gte=filters['min_member'])
    if filters.get('max_member'):
        carpools = carpools.filter(member__lte=filters['max_member'])
    if filters.get('min_price'):
        carpools = carpools.filter(price__gte=filters['min_price'])
    if filters.get('max_price'):
        carpools = carpools.filter(price__lte=filters['max_price'])
    if filters.get('carpool_date'):
        carpools = carpools.filter(carpool_date__date=filters['carpool_date'])

    serializer = CarpoolSerializer(carpools, many=True)
    return Response({'carpools': serializer.data})
