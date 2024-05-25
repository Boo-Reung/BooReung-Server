from .models import Carpool, CompletedCarpool, Caution
from rest_framework import serializers

class CarpoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpool
        fields = [
            'id', 'title', 'type', 'client_gender', 'dept', 'dest', 
            'member', 'price', 'created_at', 'carpool_date'
            ]

class CarpoolDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpool
        fields = [
            'id', 'post_num', 'host_name', 'title', 'type', 'client_gender',
            'host_gender', 'dept', 'dest', 'member', 'price', 'car_info',
            'content', 'open_kakao', 'created_at', 'carpool_date'
        ]