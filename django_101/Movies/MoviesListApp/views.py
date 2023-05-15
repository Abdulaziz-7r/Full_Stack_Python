from django.shortcuts import render
from .models import Movie_info
from .utils import avg_rate

def Movies_list(request):
    movies = Movie_info.objects.all()
    movies_list = []
    for movie in movies:
        reviews = movie.review_set.all()
        if reviews:
            movie_rating = avg_rate([review.rating for review in reviews])
            num_reviews = len(reviews)
        else:
            movie_rating = None
            num_reviews = 0
        movies_list.append({'Movie': movie, 'movie_rating' : movie_rating, 'num_reviews' : num_reviews})
    
    context = {'Movies_list' : movies_list}
    return render(request, 'MoviesListApp/Movies_list.html', context)
