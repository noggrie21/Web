from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Movie

def index(request):
    movies = Movie.objects.order_by('pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)