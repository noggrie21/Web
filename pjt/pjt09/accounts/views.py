from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        signupform = CustomUserCreationForm(request.POST)
        if signupform.is_valid():
            signupform.save()
            return redirect('movies:index')
    else:
        signupform = CustomUserCreationForm()
    context = {
        'signupform': signupform,
    }
    return render(request, 'accounts/signup.html', context)


@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')
        
    if request.method == 'POST':
        loginform = AuthenticationForm(request, data=request.POST)
        if loginform.is_valid():
            auth_login(request, loginform.get_user())
            print('여기여기여기')
            return redirect('movies:index')
    else:
        loginform = AuthenticationForm()
    context = {
        'loginform': loginform,
    }
    return render(request, 'accounts/login.html', context)