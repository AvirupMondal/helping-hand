from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserNew(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    contact=models.CharField(max_length=15)
    address=models.CharField(max_length=15)
    state=models.CharField(max_length=15)
    city=models.CharField(max_length=15)
    pincode=models.CharField(max_length=15)
    category=models.CharField(max_length=15)