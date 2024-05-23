from .models import Carpool, CompletedCarpool, Caution
from rest_framework import serializers
#성사된 카풀 정보 입력
class InfoSerializer(serializers.Serializer):
    client_name=serializers.CharField(max_length=10)
    student_num=serializers.CharField(max_length=9)
    phone_num=serializers.CharField(max_length=11)
    post_num=serializers.IntegerField()
    host_name=serializers.CharField(max_length=10)
    host_phone_num=serializers.CharField(max_length=11)
    car_info=serializers.CharField(max_length=50)
    carpool_date=serializers.DateTimeField()


#카풀 주최하기
class Carpool(serializers.Serializer):
    post_num = serializers.IntegerField()
    host_name = serializers.CharField(max_length=255)
    title = serializers.CharField(max_length=255)
    type = serializers.CharField(max_length=255)
    client_gender = serializers.CharField(max_length=255)
    host_gender = serializers.CharField(max_length=255)
    dept = serializers.CharField(max_length=255)
    dest = serializers.CharField(max_length=255)
    member = serializers.IntegerField()
    price = serializers.IntegerField()
    car_info = serializers.CharField(max_length=255)
    content = serializers.CharField()
    open_kakao = serializers.CharField()
    created_at = serializers.DateTimeField(auto_now_add=True)
    end_carpool = serializers.BooleanField(default=False)
    carpool_date = serializers.DateTimeField()
