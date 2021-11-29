from django import forms
from .models import ContactUs

class ContactUsForm(forms.ModelForm):
	class Meta:
		model = ContactUs
		fields = '__all__'


		widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter a name'}),
		'tel': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter a phone number'}),
		'email': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter a email'}),
		'info': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter extra informations'})
		}

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateSignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

		widgets = {
		'username': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter a name'}),
		'email': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Enter email'}),
		'password1': forms.PasswordInput(attrs={'class': 'form-control mb-3'}),
		'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':
                                                                'Repeat your passphrase'}),
		}
