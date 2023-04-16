from django.db import models
import uuid
from django.urls.base import reverse
# Create your models here.
class Image_Store(models.Model):
    left=models.FileField(upload_to='documents/')
    right=models.FileField(upload_to='documents/')
    lasteat=models.IntegerField(name="lasteat")
    class Meta:
        db_table='Image_Store'