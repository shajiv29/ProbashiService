from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save
import random

# Create your models here.

class Student(models.Model):
    GENDER_LIST = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=60)
    student_fathers_name = models.CharField(max_length=50)
    student_mothers_name = models.CharField(max_length=50)
    student_gender = models.CharField(max_length=10, choices=GENDER_LIST)
    student_date_of_birth = models.DateField(default=None)
    student_email = models.EmailField(blank=True, null=True)
    student_passport_number = models.CharField(max_length=10, blank=True, null=True)
    student_mobile_no = models.CharField(max_length=15, blank=True, null=True)
    student_image = models.FileField(upload_to='documents/student_image', blank=True, null=True)
    student_slug = models.SlugField(unique=True)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        self.student_slug = slugify(self.student_name)
        super(Student, self).save(*args, **kwargs)


class Education(models.Model):
    BOARD_LIST = (
        ('dhaka', 'Dhaka'),
        ('cumilla', 'Cumilla'),
        ('barisal', 'Barisal'),
        ('chittagong', 'Chittagong'),
        ('dinajpur', 'Dinajpur'),
        ('jessore', 'Jessore'),
        ('rajshahi', 'Rajshahi'),
        ('mymensingh', 'Mymensingh'),
        ('sylhet', 'Sylhet'),
        ('madrasah', 'Madrasah'),
        ('technical', 'Technical'),
        ('university', 'University')
    )
    education_id = models.AutoField(primary_key=True)
    degree = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    board = models.CharField(max_length=15, choices=BOARD_LIST)
    institute = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class PresentAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    division = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    upazila = models.CharField(max_length=20)
    thana = models.CharField(max_length=20)
    village = models.CharField(max_length=20)
    house_no = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=20)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class PermanentAddress(models.Model):
    address_id = models.AutoField(primary_key=True)
    division = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    upazila = models.CharField(max_length=20)
    thana = models.CharField(max_length=20)
    village = models.CharField(max_length=20)
    house_no = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=20)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Division(models.Model):
    id = models.AutoField(primary_key=True)
    division_name = models.CharField(max_length=20)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)

class District(models.Model):
    id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=20)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)


class Upazila(models.Model):
    id=models.AutoField(primary_key=True)
    upazila_name = models.CharField(max_length=20)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)

class Thana(models.Model):
    id = models.AutoField(primary_key=True)
    thana_name = models.CharField(max_length=20)
    upazila = models.ForeignKey(Upazila, on_delete=models.CASCADE)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)
