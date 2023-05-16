from django.contrib import admin
from .models import Movie_info, Contributor, Publisher, MovieContributor, Review

class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'email')
    list_filter = ['name']

class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'publisher')
    list_filter = ['publisher']

admin.site.register(Movie_info, MovieAdmin)
admin.site.register(Contributor)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(MovieContributor)
admin.site.register(Review)