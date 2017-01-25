from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Resume(models.Model):
	name=models.CharField(max_length=120)
	date_of_birth=models.CharField(max_length=120)
	email_ID=models.EmailField(max_length=200)
	mobile_no=models.CharField(max_length=120)
	address=models.TextField()
	#course=models.CharField(max_length=120)
	#year=models.CharField(max_length=120)
	#qualification=models.TextField()
	#achievement=models.TextField()
	#job_experience=models.TextField()
	#hobbies=models.TextField()
	#marital_status=models.CharField(max_length=120)
	#references=models.TextField()

	def __unicode__(self):
		return self.name

