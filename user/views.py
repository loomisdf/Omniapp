from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.context_processors import csrf
from user.forms import UserForm

# Create your views here.
def login(request):
    return render(request, 'login.html')

def signup(request):
	form = UserForm()
	#if this is a post request we need to process the form data
	if request.method == 'POST':
		#create a form instance and populate it with data from the request
		form = UserForm(request.POST)
		#check whether it's valid:
		if form.is_valid():
			#process the data in form.cleaned_data as required
			# ...
			# redirect to a new URL:
			form.save()
			return HttpResponseRedirect('/signup/created_user/')

		else:
			form = UserForm()

		return render(request, 'signup.html', {'form': form})

	else:
		return render(request, 'signup.html', {'form': form})

def created_user(request):
	return render(request, 'created_user.html')
