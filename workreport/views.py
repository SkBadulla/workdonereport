from django.shortcuts import render
from django.http import HttpResponse
from workreport.models import Details

# Create your views here.

def welcomeMsg(request):
	return HttpResponse('Hi,Welcome to My Page')

def home(request):
	return render(request,'workreport/home.html',{})

def details(request):
	data = Details.objects.all()
	return render(request,'workreport/details.html',{'data':data})
