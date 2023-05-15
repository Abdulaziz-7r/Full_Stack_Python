from django.contrib import admin
from .models import Movie_info
from .models import Contributor
from .models import Publisher
from .models import MovieContributor
from .models import Review

admin.site.register(Movie_info)
admin.site.register(Contributor)
admin.site.register(Publisher)
admin.site.register(MovieContributor)
admin.site.register(Review)