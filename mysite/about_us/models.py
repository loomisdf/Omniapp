from django.db import models

# Create your models here
# When you're done making models run 
# python manage.py makemigrations
# python manage.py migrate

class team_member(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    
