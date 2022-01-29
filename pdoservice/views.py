from django.shortcuts import render
from pdoservice.models import Student, PDO, Country, Payment, Batch
from pdoservice.serializers import PDOSerializer, StudentSerializer, CountrySerializer, BatchSerializer, PaymentSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

class StudentViewSets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

class PDOViewSets(viewsets.ModelViewSet):
    queryset=PDO.objects.all()
    serializer_class=PDOSerializer

class CountryViewSets(viewsets.ModelViewSet):
    queryset=Country.objects.all()
    serializer_class=CountrySerializer

class BatchViewSets(viewsets.ModelViewSet):
    queryset=Batch.objects.all()
    serializer_class=BatchSerializer

class PaymentViewSets(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class = PaymentSerializer
