from django.shortcuts import redirect, render, get_object_or_404
from .models import Movie_info, Publisher
from .utils import avg_rate
from .forms import PublisherForm
from django.contrib import messages

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

def publisher_edit(request, pk=None):
    if pk is not None:
        publisher = get_object_or_404(Publisher, pk= pk)
    else: 
        publisher = None
    
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            update_publisher = form.save()
            if publisher is None:
                messages.success(request, 'Publisher "{}" was created'.format(update_publisher))
            else:
                messages.success(request, 'Publisher "{}" was updated'.format(update_publisher))
            return redirect('publisher_edit', update_publisher.pk)
    else:
        form = PublisherForm(instance=publisher)
    return render(request, 'forms.html', {"method": request.method, "form": form})