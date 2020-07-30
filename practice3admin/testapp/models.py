from django.db import models

# Create your models here.
class Language(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Framework(models.Model):
    name=models.CharField(max_length=30)
    language = models.ManyToManyField(Language,null=True)
    def __str__(self):
        return self.name

class manufacturer(models.Model):
    manf_name=models.CharField(max_length=30)
    def __str__(self):
        return self.manf_name

class car(models.Model):
    manf_name=models.ForeignKey(manufacturer, on_delete=models.CASCADE)
    car_name = models.CharField(max_length=30)
    def __str__(self):
        return self.car_name

        