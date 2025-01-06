from django.contrib import admin
from .models import *

# Register your models here.

try:
    admin.site.register(User)
except Exception:
    print("Message from admin.py")