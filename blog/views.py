from django.shortcuts import render

#
from django.http import HttpResponse

# Create your views here.

#the route must have a request param
def home(request):
	return HttpResponse("<h1>blog - home</h1>")

def about(request):
	return HttpResponse("<h1>blog - about</h1>")




