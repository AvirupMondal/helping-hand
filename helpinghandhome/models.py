from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class usernew(models.Model):
    contact=models.CharField(max_length=50)
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    pincode=models.CharField(max_length=150)
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True)



  
