from django.contrib import admin
from django.urls import path
from .views import *
app_names = 'carpools'

urlpatterns = [
    path('host1/',PostAPIView.as_view(), name='PostAPIView'),
    path('completedhost1/' ,CompletedAPIView.as_view(), name='CompletedAPIView'),
]


#host1/: 카풀 주최하기 주소
#completedhost1/: 성사된 카풀 정보 입력 주소