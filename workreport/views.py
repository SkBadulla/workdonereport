from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def welcomeMsg(request):
	return HttpResponse('Hi,Welcome to My Page')

def home(request):
	return render(request,'workreport/home.html',{})