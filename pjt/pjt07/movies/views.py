from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from movies.forsm import MovieForm, CommentForm
from .models import Movie, Comment
from django.contrib.auth.decorators import login_required


@require_safe
def index(request):
    movies = Movie.objects.order_by('-pk')
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        movieform = MovieForm(request.POST)
        if movieform.is_valid():
            movie = movieform.save(commit=False)
            movie.user = request.user
            movie.save()
            return redirect('movies:detail', movie.pk)
    else:
        movieform = MovieForm()
    context = {
        'movieform' : movieform, 
    }
    return render(request, 'movies/create.html', context)


@require_safe
def detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    commentform = CommentForm()
    comments = movie.comment_set.all()
    context = {
        'movie': movie,
        'commentform': commentform,
        'comments': comments,
    }
    return render(request, 'movies/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user == movie.user:
        if request.method == 'POST':
            movieform = MovieForm(request.POST, instance=movie)
            if movieform.is_valid():
                movie.save()
                return redirect('movies:detail', movie.pk)
        else:
            movieform = MovieForm(instance=movie)
        context = {
            'movieform': movieform,
            'movie': movie,
        }
        return render(request, 'movies/update.html', context)
    return redirect('movies:index')


@require_POST
def delete(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user.is_authenticated:
        if movie.user == request.uer: 
            movie.delete()
    return redirect('movies:index')


@require_POST
def create_comment(request, movie_pk):
    if request.user.is_authenticated:
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.movie = get_object_or_404(Movie, pk=movie_pk)
            comment.user = request.user
            comment.save()
        return redirect('movies:detail', movie_pk)
    return redirect('accounts:login')


@require_POST
def delete_comment(request, movie_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user.is_authenticated:
        if request.user == comment.user:
            comment.delete()
    return redirect('movies:detail', movie_pk)
