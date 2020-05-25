from django.db import models

# Create your models here.
class Description(models.Model):
    name= models.CharField(max_length=25)
    email = models.EmailField()
    address = models.CharField(max_length=25)
    pincode = models.IntegerField()
    nick_name = models.CharField(max_length=20)

class PATIENT(models.Model):
    name= models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    disease = models.CharField(max_length=20)