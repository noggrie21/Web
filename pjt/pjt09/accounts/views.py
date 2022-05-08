from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import AuthenticationForm


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == 'POST':
        signupform = CustomUserCreationForm(request.POST)
        if signupform.is_valid():
            signupform.save()
            return redirect('movies:index')
    if request.method == 'GET':
        signupform = CustomUserCreationForm()
    context = {
        'signupform': signupform,
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        pass
    else:
        loginform = AuthenticationForm()