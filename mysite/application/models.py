from django.db import models
from django import forms
#from django.core.files.storage import FileSystemStorage

#fs = FileSystemStorage(location='/media/photos')

# Create your models here.

class Application(models.Model):
    title = models.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    link = models.CharField(max_length=1000)
#    logo = models.ImageField(storage=fs)

class Comment(models.Model):
    application = models.ForeignKey(Application)
    rating = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
                             


                             
