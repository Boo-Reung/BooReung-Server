from django.db import models

# Create your models here.

class Carpool(models.Model):
    post_num = models.IntegerField(null=True, blank=True)
    host_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    client_gender = models.CharField(max_length=255)
    host_gender = models.CharField(max_length=255)
    dept = models.CharField(max_length=255)
    dest = models.CharField(max_length=255)
    member = models.IntegerField()
    price = models.IntegerField()
    car_info = models.CharField(max_length=255)
    content = models.TextField()
    open_kakao = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    end_carpool = models.BooleanField(default=False)
    carpool_date = models.DateTimeField()

class CompletedCarpool(models.Model):
    client_name = models.CharField(max_length=255)
    student_num = models.CharField(max_length=255)
    phone_num = models.CharField(max_length=255)
    post_num = models.IntegerField()
    host_name = models.CharField(max_length=255)
    host_phone_num = models.CharField(max_length=255)
    car_info = models.CharField(max_length=255)
    carpool_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class Caution(models.Model):
    content = models.TextField()