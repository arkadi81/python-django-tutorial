from django.urls import path
from . import views

urlpatterns = [
	#convension - use the slash AFTER directory name, not in front
	#by default, django will redirect routes without slashes and trailing slashes as necessary
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
