from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.
def signup(request):
    return render_to_response('signup.html')

def login(request):
    return render_to_response('login.html')
