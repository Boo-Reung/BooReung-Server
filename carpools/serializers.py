from .models import Carpool, CompletedCarpool, Caution
from rest_framework import serializers

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