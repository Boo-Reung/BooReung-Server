from django.contrib import admin
from django.urls import path

from .views import RandomCautionView
from . import views


app_names = 'carpools'

urlpatterns = [
  path('caution/', RandomCautionView.as_view(), name='random-caution'),
  path('filter/', views.filter_carpools, name='filter_carpools'),
]