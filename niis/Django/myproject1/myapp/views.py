from django.http import HttpResponse
from django.shortcuts import render
def home(request):
	return render(request,'Index.html')

def about(request):
	return render(request,'about.html')



def home1(request):
	return HttpResponse("Hello,World!")

def about1(request):
	return HttpResponse("About page")

def contact(request):
	return HttpResponse("contact page")

def services(request):
	return HttpResponse("our services")

def welcome(request,name):
	return HttpResponse(f"welcome{name}|")
	
