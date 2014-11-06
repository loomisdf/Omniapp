from django.db import models
from django import forms
#from django.core.files.storage import FileSystemStorage

#fs = FileSystemStorage(location='/media/photos')

# Create your models here.

#add up the ratings and find the average
def CalculateRating():
    return 0;

class Application(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    link = models.CharField(max_length=1000)
    rating = CalculateRating()
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    application = models.ForeignKey(Application)
    rating = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
    
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username

                             
