from django.contrib import admin
from application.models import Application, Comment

class ApplicationAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'link']


# Register your models here.
admin.site.register(Application)
admin.site.register(Comment)
