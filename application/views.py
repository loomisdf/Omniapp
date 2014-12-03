from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from application.models import Application, Comment, Supported_Platform
from application.forms import ApplicationForm


# Create your views here.
def index(request):
    app_list = Application.objects.all()
    context = {'app_list': app_list}
    return render(request, 'index.html',context)

def app_detail(request, app_id):
    print(app_id)
    app = Application.objects.get(pk=app_id)
    supported_platforms_list = Supported_Platform.objects.filter(application = app_id)
    comment_list = Comment.objects.filter(application=app_id)
    context = {'app': app,
               'comment_list': comment_list,
               'supported_platforms_list': supported_platforms_list,
    }
    return render(request,'application.html', context)

def app_upload(request):
    form = ApplicationForm()
    print("hello")
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            print('saving form')
            form.save()
            return HttpResponseRedirect('/application/app_upload_complete/')

        else: 
            print("dat form aint valid")
            print(form.errors)
            form = ApplicationForm()

        return render(request, 'app_upload.html', {'form': form})

    else: 
        return render(request, 'app_upload.html', {'form': form})

def app_upload_complete(request):
    return render(request, 'app_upload_complete.html')