from django.db import models

# Create your models here.
class ImageUploading(models.Model):
    image_upload=models.ImageField(default='example.png',upload_to='images/',null=True,blank=True)