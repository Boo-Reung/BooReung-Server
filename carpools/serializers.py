from .models import Carpool, CompletedCarpool, Caution
from rest_framework import serializers

class CautionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caution
        fields = ['content']
