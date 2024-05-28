from django.contrib import admin
from django.urls import path
from .views import CarpoolListView, carpool_detail
from . import views

#host1/: 카풀 주최하기 주소
#completedhost1/: 성사된 카풀 정보 입력 주소 

from .views import *

app_names = 'carpools'

urlpatterns = [

    path('full_list/', CarpoolListView.as_view(), name = 'carpool_list_48hours'),
    path('detail/<int:pk>/', views.carpool_detail, name = 'carpool_detail'),

    path('caution/', RandomCautionView.as_view(), name='random-caution'),
    path('filter/', filter_carpools, name='filter_carpools'),
    path('host/',PostAPIView.as_view(), name='PostAPIView'),
    path('completedcarpool/' ,CompletedAPIView.as_view(), name='CompletedAPIView'),
]

