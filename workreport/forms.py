from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from workreport.models import Details,Profile
from django import forms
# from functools import partial
# DateInput = partial(forms.DateInput, {'class': 'datepicker'})
class DetailsForm(ModelForm):
	class Meta:
		model = Details
		fields = ['programName','collegeName','districName','startDate','endDate','refernceLink']


class DetailsFormWd(forms.Form):
	programName = forms.CharField(label = "Program Name",
		widget=forms.TextInput(attrs={"class":'form-control','placeholder':"Enter program Name"}))
	collegeName = forms.CharField(label = "College Name",
		widget=forms.TextInput(attrs={"class":'form-control','placeholder':"Enter College Name"}))
	districName = forms.CharField(label = "District Name",
		widget=forms.TextInput(attrs={"class":'form-control','placeholder':"Enter DistrictName"}))
	startDate = forms.DateField(label = 'Start Date',
		widget = forms.DateInput(attrs={'class':'form-control datepicker','placeholder':'Select Start Date'}))
	endDate = forms.DateField(label = 'End Date',
		widget = forms.DateInput(attrs={'class':'form-control datepicker','placeholder':'Select End Date'}))
	refernceLink = forms.CharField(label = "Reference Name",
		widget=forms.TextInput(attrs={"class":'form-control','placeholder':"Enter Reference Name"}))



class UsersignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username','email','password1','password2']


class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = ['age','phoneNo','gender','picture','date_of_birth']








