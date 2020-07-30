from django.db import models

# Create your models here.
class person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self):
        return self.first_name

class Family(models.Model):
    id = models.IntegerField(primary_key=True)
    name= models.CharField(max_length=30)
    age = models.IntegerField()
    class Meta:
        ordering=['-id']
    def __str__(self):
        return (self.name)

class Person_shirts(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
    def __str__(self):
        return self.name


class school_student(models.Model):
    name= models.CharField(max_length=30)
    class_choices=((1,'first'),(2,'second'),(3,'third'),(4,'fourth'))
    study = models.IntegerField(choices=class_choices)
    def __str__(self):
        return self.name

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ['headline']