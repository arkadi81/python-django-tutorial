from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
#the route must have a request param

#dummy data for demonstration to pass info to templates
posts = [
	{
		'author': 'ark1',
		'title': 'post1',
		'content': 'post1 content',
		'date': 'oct 20,2019'
	},
	{
		'author': 'ark2',
		'title': 'post2',
		'content': 'post2 content',
		'date': 'oct 21,2019'
	}
]
def home(request):
	#the context is our way of passing arguments to the template
	#the key will be accessible in the template
	context = {
		'posts': posts,
		'title': 'Django project'
	}
	#django shortcut to load in a template
	return render(request, 'blog/home.html',context)
	# there's a third optional context parameter that allows us to pass info to the template.
	# views must always return either httpresponse or exception.

	# return HttpResponse("<h1>blog - home</h1>")

def about(request):
	return render(request, 'blog/about.html')
	# return HttpResponse("<h1>blog - about</h1>")




