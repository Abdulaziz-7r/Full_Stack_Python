from django.db import models

class Movie_info(models.Model):
    name = models.CharField(max_length=100, help_text= 'Name of movie')
    date = models.DateField(verbose_name='Movie released date')
    
