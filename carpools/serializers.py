from .models import Carpool, CompletedCarpool, Caution
from rest_framework import serializers

class CarpoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carpool
        fields = ['post_num', 'title', 'type', 'client_gender','dept', 'dest', 'member', 'price', ,'carpool_date', 'created_at', 'end_carpool', 'CarpoolListView']