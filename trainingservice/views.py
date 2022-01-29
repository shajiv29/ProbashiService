from django.shortcuts import render
from trainingservice.models import TrainingCenter
from trainingservice.serializers import TrainingCenterSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
class TrainingCenerViewSet(viewsets.ModelViewSet):
    queryset = TrainingCenter.objects.all()
    serializer_class=TrainingCenterSerializer
