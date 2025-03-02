from django.db import models

class info(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=500,default="Nothing was submitted by this user")
    
# Create your models here.

