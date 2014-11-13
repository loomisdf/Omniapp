from django.contrib import admin
from application.models import Application, Comment, User

class CommentInline(admin.TabularInline):
    model = Comment
    fields = ['title', 'rating', 'description']
    
class ApplicationAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'link', 'price']
    inlines = [CommentInline]
    list_display = ('title','rating')
    search_fields = ['title']

# Register your models here.
admin.site.register(Application, ApplicationAdmin)
admin.site.register(User)
