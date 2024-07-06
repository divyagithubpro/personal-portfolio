from django.db import models

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.CharField(max_length=25)
    subject=models.CharField(max_length=25)
    message=models.CharField(max_length=25)