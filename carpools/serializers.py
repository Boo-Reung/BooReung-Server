from .models import Carpool, CompletedCarpool, Caution
from rest_framework import serializers

class CarpoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpool
        fields = ['id', 'created_at', 'end_carpool', 'CarpoolListView']