from django.contrib import admin
from django.urls import path

from .views import RandomCautionView


app_names = 'carpools'

urlpatterns = [
  path('api/caution/', RandomCautionView.as_view(), name='random-caution'),

]