from .models import TrainingCenter, Trade
from rest_framework import serializers


class TrainingCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model=TrainingCenter
        fields='__all__'


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trade
        fields='__all__'
