from django.shortcuts import render
from .models import Movie_info

def Movies_list(request):
    movies = Movie_info.objects.all()
    movies_list = []
    for movie in movies:
        movies_list.append({'Movie': movie})
    
    context = {'Movies_list' : movies_list}
    return render(request, 'MoviesListApp/Movies_list.html', context)
