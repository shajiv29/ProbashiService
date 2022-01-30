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

class Trade(models.Model):
    trade_id = models.AutoField(primary_key=True)
    trade_name = models.CharField(max_length=50)
    trade_slug = models.SlugField(unique=True, null=True)
    is_active = models.NullBooleanField(default=False)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)

    def save(self, *args, **kwargs):
        self.trade_slug = slugify(self.trade_name)
        super(Trade, self).save(*args, **kwargs)


# class AssignTrade(models.Model):
#     assign_trade_id = models.AutoField(primary_key=True)
#     assign_ttc = models.ForeignKey(TrainingCenter, on_delete=models.CASCADE)
#     assign_trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
#     is_active = models.NullBooleanField(default=True)
#     is_delete = models.NullBooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True, null=True)
#     modified = models.DateTimeField(auto_now_add=True, null=True)


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_start_date = models.DateField()
    session_end_date = models.DateField()
    session_capacity = models.IntegerField(null=True, blank=True)
    interview_date = models.DateField()
    application_last_date = models.DateField()
    interview_result_date = models.DateField()
    trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    is_active = models.NullBooleanField(default=True)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)


class TradeAssign(models.Model):
    assign_training_center = models.ForeignKey(TrainingCenter, on_delete=models.CASCADE)
    assign_trade = models.ForeignKey(Trade, on_delete=models.CASCADE)
    is_active = models.NullBooleanField(default=True)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)

class Batch(models.Model):
    batch_id = models.AutoField(primary_key=True)
    batch_name = models.CharField(max_length=20)
    batch_size = models.IntegerField()
    class_start_date = models.DateField()
    trade_assign = models.ForeignKey(TradeAssign, on_delete=models.CASCADE)
    is_active = models.NullBooleanField(default=True)
    is_delete = models.NullBooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, null=True)
    modified = models.DateTimeField(auto_now_add=True, null=True)
