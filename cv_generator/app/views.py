from django.shortcuts import render
from models import *
from django.http import *
# Create your views here.

def home(request):
	return render(request,'home.html')


def generate(request):
	name=request.POST['name']
	dob=request.POST['date_of_birth']
	email=request.POST['email_ID']
	mobile=request.POST['mobile_no']
	address=request.POST['address']
	query=Resume(name=name,date_of_birth=dob,email_ID=email,mobile_no=mobile,address=address) 
	query.save()

	return HttpResponse("Success")
