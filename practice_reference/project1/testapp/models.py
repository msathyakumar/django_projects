from django.db import models

# Create your models here.
class Details_model(models.Model):
    username= models.CharField(max_length=30)
    address= models.CharField(max_length=30)
    pincode = models.IntegerField()

    def __str__(self):
        return self.username

class new_model(models.Model):
    Name= models.CharField(max_length=30)
    age= models.IntegerField()
    email = models.EmailField()
    profile = models.ImageField(null=True)
    date_of_birth = models.DateField(null=True)
    description = models.TextField()
    small_int_field = models.IntegerField(default=True,null=True)
    def _str__(self):
        return self.Name



class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline