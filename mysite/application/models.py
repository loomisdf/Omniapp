from django.db import models
from django import forms
#from django.core.files.storage import FileSystemStorage

#fs = FileSystemStorage(location='/media/photos')

# Create your models here.

class Application(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    link = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title
#    logo = models.ImageField(storage=fs)



class Comment(models.Model):
    application = models.ForeignKey(Application)
    rating = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title
    


                             
