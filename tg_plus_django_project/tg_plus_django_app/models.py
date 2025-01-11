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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField()
    brand = models.CharField()
    ratings = models.JSONField(blank=True, null=True)
    images_paths = models.JSONField()
