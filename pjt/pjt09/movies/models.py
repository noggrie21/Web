from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    release_date = models.TextField()
    popularity = models.FloatField()
    overview = models.TextField()
    poster_path = models.TextField()

class Genre(models.Model):
    name = models.CharField(max_length=20)
    movies = models.ManyToManyField(Movie, related_name="genres")
