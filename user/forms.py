from django.forms import ModelForm
from myapp.models import Article

#form class 

class UserForm():
	class Meta:
		model = User
		fields = ['username', 'password', 'email']