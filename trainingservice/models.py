from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify


# Create your models here.
class TrainingCenter(models.Model):
    center_id = models.AutoField(primary_key=True)
    center_name = models.CharField(max_length=100)
    center_mobile_no = models.CharField(max_length=15)
    center_mobile_no_2 = models.CharField(max_length=15, blank=True, null=True)
    center_email = models.EmailField(max_length=100)
    center_address = models.CharField(max_length=250)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    district = models.CharField(max_length=30)
    division = models.CharField(max_length=30)
    thana = models.CharField(max_length=30, blank=True, null=True)
    photo = models.FileField(upload_to='documents/trining_center_image', blank=True, null=True)
    center_slug = models.SlugField(unique=True)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        self.center_slug = slugify(self.center_name)
        super(TrainingCenter, self).save(*args, **kwargs)
