from django.shortcuts import render
from models import *
from django.http import *
from reportlab.pdfgen import canvas
from django.http import HttpResponse
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
	
    # Create the HttpResponse object with the appropriate PDF headers.
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="Resume.pdf"'

    # Create the PDF object, using the response object as its "file."
	p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
	p.setFont("Helvetica",10)
	p.drawString(150, 830, "Name : "+name)
	p.setFont("Helvetica",10)
	p.drawString(150, 810, "Date of Birth :"+dob)
	p.setFont("Helvetica",10)
	p.drawString(150, 790, "Email ID :"+email)
	p.setFont("Helvetica",10)
	p.drawString(150, 770, "Mobile No. :"+mobile)
	p.setFont("Helvetica",10)
	p.drawString(150, 750, "Address :"+address)


    # Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()	
	
	# return HttpResponse(pdf, 'application/pdf')

	return response
