from django.contrib import admin
from application.models import Application

class ApplicationAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'link']

# Register your models here.
admin.site.register(Application)
