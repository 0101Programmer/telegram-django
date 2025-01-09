from django.contrib import admin
from .models import *

# Register your models here.

try:
    admin.site.register(User)
    admin.site.register(Product)
except Exception:
    print("Message from admin.py")