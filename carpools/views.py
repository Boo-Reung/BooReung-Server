from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

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
            carpool.end_carpool == True
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
    if filters.get('client_gender'):
        carpools = carpools.filter(client_gender=filters['client_gender'])
    if filters.get('dept'):
        carpools = carpools.filter(dept=filters['dept'])
    if filters.get('dest'):
        carpools = carpools.filter(dest=filters['dest'])
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