from django.shortcuts import render
from .models import Education, Student, PresentAddress, Thana, Division, PermanentAddress, District, Upazila
from .serializers import EducationSerializer, StudentSerializer, PresentAddressSerializer, ThanaSerializer, DivisionSerializer, PermanentAddressSerializer, DistrictSerializer, UpazilaSerializer
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class PresentAddressViewSet(viewsets.ModelViewSet):
    queryset = PresentAddress.objects.all()
    serializer_class = PresentAddressSerializer

class PermanentAddressViewSet(viewsets.ModelViewSet):
    queryset = PermanentAddress.objects.all()
    serializer_class = PermanentAddressSerializer

class ThanaViewSet(viewsets.ModelViewSet):
    queryset = Thana.objects.all()
    serializer_class = ThanaSerializer

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class DistricViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class UpazilaViewSet(viewsets.ModelViewSet):
    queryset = Upazila.objects.all()
    serializer_class = UpazilaSerializer
