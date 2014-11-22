from django.forms import ModelForm
from user.models import User

#form class 
class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password', 'email']