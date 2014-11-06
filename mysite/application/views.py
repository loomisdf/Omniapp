from django.shortcuts import render
from django.http import HttpResponse
from application.models import Application


# Create your views here.
def index(request):
    app_list = Application.objects.all()
    context = {'app_list': app_list}
    return render(request, 'index.html',context)

def app_detail(request, app_id):
    print(app_id)
    app = Application.objects.get(pk=app_id)
    context = {'app': app}
    return render(request,'application.html', context)
