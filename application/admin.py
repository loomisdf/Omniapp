from django.contrib import admin
from application.models import Application, Comment, Supported_Platform

class PlatformInline(admin.TabularInline):
    model = Supported_Platform
    fields = ['title']

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['title', 'rating', 'description']
    
class ApplicationAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'link', 'price', 'photo']
    inlines = [ PlatformInline, CommentInline]
    list_display = ('title','rating')
    search_fields = ['title']


    
# Register your models here.
admin.site.register(Application, ApplicationAdmin)
