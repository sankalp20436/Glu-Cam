from django.contrib import admin

from .models import Image_Store

# Register your models here.
"""
In this way we register the created model in the admin app. 
"""
admin.site.register(Image_Store)