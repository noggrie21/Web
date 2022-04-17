from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        userform = CustomUserCreationForm(request.POST)
        if userform.is_valid():
            user = userform.save()
            auth_login(request, user)
            return redirect('movies:index')
    else:
        userform = CustomUserCreationForm()
    context = {
        'userform': userform,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        loginform = AuthenticationForm(request, request.POST)
        if loginform.is_valid():
            auth_login(request, loginform.get_user())
            return redirect(request.GET.get('next') or 'movies:index')
    else:
        loginform = AuthenticationForm()
    context = {
        'loginform': loginform,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('movies:index')

