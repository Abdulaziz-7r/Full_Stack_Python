from django.db import models
from django.contrib import auth

class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text= 'name of publisher')
    website = models.URLField(help_text="publisher's website")
    email = models.EmailField(help_text="publisher's email")

class Movie_info(models.Model):
    name = models.CharField(max_length=100, help_text= 'Name of movie')
    date = models.DateField(verbose_name='Movie released date')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributor = models.ManyToManyField('Contributor', through= "MovieContributor")

    def __str__(self):
        return self.name
    
class Contributor(models.Model):
    first_name = models.CharField(max_length=50, help_text= "contributor's first name")
    last_name = models.CharField(max_length=50, help_text= "contributor's last name")
    email = models.EmailField(help_text="contributor's email")

    def __str__(self):
        return self.first_name

class MovieContributor(models.Model):
    class ContributionRole(models.TextChoices):
        ACTOR = "ACTOR", "Actor"
        DIRECTOR = "DIRECTOR", "Director"
    movie = models.ForeignKey(Movie_info, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name= "contributor's role in the movie", choices= ContributionRole.choices, max_length=20)

class Review(models.Model):
    content = models.TextField(help_text="review text")
    rating = models.IntegerField(help_text="rating that given by reviewer")
    date_created = models.DateTimeField(auto_now_add=True, help_text="date and time of the review")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie_info, on_delete=models.CASCADE, help_text="the movie that this review is for")