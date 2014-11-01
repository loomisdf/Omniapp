from django.contrib import admin
from application.models import Application, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['title', 'rating', 'description']
    
class ApplicationAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'link']
    inlines = [CommentInline]

# Register your models here.
admin.site.register(Application, ApplicationAdmin)
