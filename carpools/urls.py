from django.contrib import admin
from django.urls import path
from .views import CarpoolListView, carpool_detail
from . import views

app_names = 'carpools'

urlpatterns = [
    path('full_list/', CarpoolListView.as_view(), name = 'carpool_list_48hours'),
    path('detail/<int:pk>/', views.carpool_detail, name = 'carpool_detail'),
]