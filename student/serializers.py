from .models import Education, Student, PresentAddress, Thana, Division, PermanentAddress, District, Upazila
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Education
        fields='__all__'

class PresentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=PresentAddress
        fields='__all__'

class ThanaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Thana
        fields='__all__'

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Division
        fields='__all__'

class PermanentAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=PermanentAddress
        fields='__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model=District
        fields='__all__'

class UpazilaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Upazila
        fields='__all__'
