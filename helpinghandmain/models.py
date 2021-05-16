from django.db import models

# Create your models here.


class Register(models.Model):

    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    password=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    state=models.CharField(max_length=500)
    city=models.CharField(max_length=500)
    pincode=models.CharField(max_length=500)
    category=models.CharField(max_length=500)
    contact=models.CharField(max_length=20)
    

    def __str__(self):
        return 'New User' + self.name + (self.category)