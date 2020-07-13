from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

from workreport.models import Details,Profile
from workreport.forms import DetailsFormWd,DetailsForm,UsersignupForm,ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def welcomeMsg(request):
	return HttpResponse('Hi,Welcome to My Page')

def home(request):
	return render(request,'workreport/home.html',{})

def signUp(request):
	if request.method=='POST':
		form = UsersignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	form  = UsersignupForm()
	return render(request,'workreport/signUp.html',{'form':form})

@login_required
def getinfo(request,pk):
	data = Details.objects.filter(user_id=pk)
	return render(request,'workreport/details.html',{'data':data})
@login_required
def addDetails(request,pk):
	data = User.objects.get(id=pk)
	form  = DetailsForm()
	if request.method == 'POST':
		formdata = DetailsForm(request.POST)
		print('ok')
		if formdata.is_valid():
			print('i am here')
			f=formdata.save(commit=False)
			f.user_id = data.id
			f.save()
			messages.success(request, 'Details Addedd Successfully...')
			return render(request,'workreport/addDetails.html',{'form':form})
		return HttpResponse('Something is wrong..')
	
	return render(request,'workreport/addDetails.html',{'form':form})


@login_required
def profile(request,pk):
	data = User.objects.get(id=pk)
	if request.method=='POST':
		info = Profile.objects.filter(user_id = pk).first()
		if info:
			form = ProfileForm(request.POST,request.FILES,instance=info)
			if form.is_valid():
				form.save()
				return redirect('home')
			print('i am')
		else:
			form = ProfileForm(request.POST,request.FILES)
			if form.is_valid():
				print('i am here'+ str(pk)	 +' '+ request.POST['phoneNo'])
				try:
					f=form.save(commit=False)
					f.user_id = data.id
					f.save()
					return redirect("home")
				except:
					return HttpResponse("<script>window.alert('something wrong')</script>")
	else:
		info = Profile.objects.filter(user_id = pk).first()
		if(info):
			print('i came to here')
			form = ProfileForm(instance=info)
			return render(request,'workreport/profile.html',{'form':form,'data':data}) 
		else:
			form = ProfileForm()
			return render(request,'workreport/profile.html',{'form':form,'data':data}) 
