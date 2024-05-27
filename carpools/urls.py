from django.contrib import admin
from django.urls import path

from .views import *

app_names = 'carpools'

urlpatterns = [
  path('caution/', RandomCautionView.as_view(), name='random-caution'),
  path('filter/', filter_carpools, name='filter_carpools'),
]