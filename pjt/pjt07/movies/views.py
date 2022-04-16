from django.shortcuts import render
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from movies.forsm import MovieForm
from .models import Movie
from django.contrib.auth.decorators import login_required

@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        pass
    else:
        movieform = MovieForm()
    context = {
        'movieform' : movieform, 
    }
    return render(request, 'movies/create.html', context)