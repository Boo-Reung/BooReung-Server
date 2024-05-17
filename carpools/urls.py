from django.contrib import admin
from django.urls import path
from .views import CarpoolListView

app_names = 'carpools'

urlpatterns = [
    path('carpools/', CarpoolListView.as_view(), name = 'carpool_list'),
]