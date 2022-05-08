from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=20)


class Movie(models.Model):
    title = models.CharField(max_length=100, unique=True)
    release_date = models.TextField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')

