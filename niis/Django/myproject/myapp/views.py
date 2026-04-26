from django.http import HttpResponse
def home(request):
	return HttpResponse("Hello World")


def about(request):
	return HttpResponse("About page")

def contact(request):
	return HttpResponse("contact page")

def services(request):
	return HttpResponse("our service")

def welcome(request,name):
	return HttpResponse(f"welcome{name}|")
