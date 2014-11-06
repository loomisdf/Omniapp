from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world, You're at the Application index.")

def app_detail(request, app_id):
    return HttpResponse("You're looking at %s." % app_id)
