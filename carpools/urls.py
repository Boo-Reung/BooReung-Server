from django.contrib import admin
from django.urls import path

#host1/: 카풀 주최하기 주소
#completedhost1/: 성사된 카풀 정보 입력 주소 

from .views import *

app_names = 'carpools'

urlpatterns = [
    path('caution/', RandomCautionView.as_view(), name='random-caution'),
    path('filter/', filter_carpools, name='filter_carpools'),
    path('host/',PostAPIView.as_view(), name='PostAPIView'),
    path('completedcarpool/' ,CompletedAPIView.as_view(), name='CompletedAPIView'),
]

