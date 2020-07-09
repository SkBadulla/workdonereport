from django.db import models

# Create your models here.

class Details(models.Model):
	programName = models.CharField(max_length=100)
	collegeName = models.CharField(max_length=100)
	districName = models.CharField(max_length=100)
	startDate = models.DateField()
	endDate = models.DateField()
	refernceLink = models.CharField(max_length=200)

	def __str__(self):
		return self.programName+' '+collegeName
	
