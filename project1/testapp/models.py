from django.db import models

# Create your models here.
class Details_model(models.Model):
    username= models.CharField(max_length=30)
    address= models.CharField(max_length=30)
    pincode = models.IntegerField()

    def __str__(self):
        return self.username