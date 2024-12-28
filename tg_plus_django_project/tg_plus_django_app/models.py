import datetime

from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField()
    email = models.EmailField(unique=True)
    password = models.CharField()
    tg_username = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    orders = models.JSONField(blank=True, null=True)
    created_at = models.CharField(default=datetime.datetime.now().astimezone().strftime("%Y-%m-%d | %H:%M:%S %z | %Z"))
    updated_at = models.CharField(default=datetime.datetime.now().astimezone().strftime("%Y-%m-%d | %H:%M:%S %z | %Z"))
    user_data = models.JSONField(blank=True, null=True)


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    model_name = models.TextField()
    model_name_for_customer = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField()
    images_paths = models.JSONField()
