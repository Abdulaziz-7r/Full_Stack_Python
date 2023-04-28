from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie_info

def Movie_name(request):
    name = "Harry Potter"
    return render(request,'base.html',{"name": name})

def welcome_page(request):
    massage = f'<html> <h1> Welcome to MoviesListApp </h1>'\
              f'<p> MoviesListApp has {Movie_info.objects.count()}</p>'\
              f'</html>'
    return HttpResponse(massage)
