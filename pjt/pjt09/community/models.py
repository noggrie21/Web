from django.db import models
from movies.models import Movie
from django.conf import settings


User = settings.AUTH_USER_MODEL


class Review(models.Model):
    title = models.CharField(max_length=100)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, db_column='movie_title', to_field='title')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked = models.ManyToManyField(User, related_name="liking")


class Comment(models.Model):
    content = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

