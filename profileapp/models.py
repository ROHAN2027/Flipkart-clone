from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/',blank=True,null=True,default='profile_pics/default.png')
    dob = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)
    def __str__(self):
        return self.user.username
# Create your models here.
