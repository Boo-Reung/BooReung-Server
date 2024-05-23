from django.contrib import admin
from django.urls import path
from carpools import views

app_names = 'carpools'

urlpatterns = [
    path('[POST1]기본주소URL/',views.PostAPIView, name='PostAPIView'),
    path('[POST2]기본주소URL/',views.CompletedAPIView, name='CompletedAPIView'),
]


#[POST1]: 카풀 주최하기 주소
#[POST2]: 성사된 카풀 정보 입력 주소