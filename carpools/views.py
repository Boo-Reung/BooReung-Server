from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Carpool, CompletedCarpool, Caution

from .serializers import CautionSerializer

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
