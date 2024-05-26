from django.contrib import admin
from django.urls import path
from .views import *
app_names = 'carpools'

urlpatterns = [
    path('post1/',PostAPIView.as_view(), name='PostAPIView'),
    path('post2/' ,CompletedAPIView.as_view(), name='CompletedAPIView'),
]


#post1/: 카풀 주최하기 주소
#post2/: 성사된 카풀 정보 입력 주소