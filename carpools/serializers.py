from .models import Carpool, CompletedCarpool, Caution
from rest_framework import serializers

#성사된 카풀 정보 입력
class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedCarpool
        fields = '__all__'



#카풀 주최하기
class Carpool(serializers.ModelSerializer):
    class Meta:
        model = Carpool
        fields = '__all__'


# CautionSerializer
class CautionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caution
        fields = ['content']

# CarpoolSerializer
class CarpoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpool
        fields = ['id', 'title', 'type', 'client_gender', 'dept', 'dest', 'member', 'price', 'created_at', 'carpool_date']

