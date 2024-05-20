from django.contrib import admin
from django.urls import path
from .views import CarpoolListView
from .import views

app_names = 'carpools'

urlpatterns = [
    path('carpools/', CarpoolListView.as_view(), name = 'carpool_list_48hours'),
    path('carpools/<int:pk>/', views.carpool_detail, name = 'carpool_detail'),
]