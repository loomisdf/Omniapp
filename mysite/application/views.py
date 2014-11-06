from django.shortcuts import render
from django.http import HttpResponse
from application.models import Application, Comment


# Create your views here.
def index(request):
    app_list = Application.objects.all()
    context = {'app_list': app_list}
    return render(request, 'index.html',context)

def app_detail(request, app_id):
    print(app_id)
    app = Application.objects.get(pk=app_id)
    comment_list = Comment.objects.filter(application=app_id)
    context = {'app': app,
               'comment_list': comment_list,}
    return render(request,'application.html', context)
