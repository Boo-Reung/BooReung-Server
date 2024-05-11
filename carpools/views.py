from django.shortcuts import render
from rest_framework.views import APIView

from .models import Carpool, CompletedCarpool, Caution


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

# 아래에 여러분의 기능을 구현해주세요...화이팅!
