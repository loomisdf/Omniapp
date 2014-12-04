from django.forms import ModelForm
from application.models import Application

#form class 
class ApplicationForm(ModelForm):
	class Meta: 
		model = Application
		fields = ['title','description', 'link', 'price', 'photo']