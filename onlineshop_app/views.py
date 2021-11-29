from django.shortcuts import render, redirect
from .models import ContactUs, Fikrlar
from .forms import ContactUsForm,CreateSignUpForm
from django import http

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def contact_us(request):

	fikrlar = Fikrlar.objects.all()

	form = ContactUsForm()
	if request.method == 'POST':
		form = ContactUsForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/')
			

	context = {'form':form, 'fikrlar':fikrlar}
	return render(request, 'index.html', context)

@login_required(login_url='login')
def buy(request):
	return render(request, 'buy.html')

@login_required(login_url='login')
def about(request):
	return render(request, 'about.html')

def signUp(request):
	form = CreateSignUpForm()
	if request.method == 'POST':
		form = CreateSignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context = {'form': form}
	return render(request, 'signup.html', context)

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/')
	return render(request, 'login.html')

def logOutPage(request):
	logout(request)
	return redirect('/login/')