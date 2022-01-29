from .models import Student, PDO, Country, Payment, Batch
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class PDOSerializer(serializers.ModelSerializer):
    class Meta:
        model=PDO
        fields='__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields='__all__'

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Batch
        fields='__all__'
