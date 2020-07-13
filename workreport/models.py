from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Details(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	programName = models.CharField(max_length=100)
	collegeName = models.CharField(max_length=100)
	districName = models.CharField(max_length=100)
	startDate = models.DateField()
	endDate = models.DateField()
	refernceLink = models.CharField(max_length=200) 
	
	def __str__(self):
		return self.programName+' '+self.collegeName
	
class Profile(models.Model):
	vals = [('Male','Male'),('FeMale','FeMale')]
	age = models.IntegerField(null=True)
	phoneNo = models.CharField(max_length=10)
	gender = models.CharField(max_length=10,choices=vals)
	picture = models.ImageField(upload_to='profilepics/',null=True)
	date_of_birth = models.DateField(null=True)
	user = models.OneToOneField(User,on_delete=models.CASCADE)


	def __str__(self):
		return self.phoneNo
