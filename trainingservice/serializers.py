from .models import TrainingCenter
from rest_framework import serializers


class TrainingCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model=TrainingCenter
        fields='__all__'
