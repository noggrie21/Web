from django.shortcuts import get_object_or_404, render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash


User = get_user_model()


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == 'POST':
        signupform = CustomUserCreationForm(request.POST)
        if signupform.is_valid():
            user = signupform.save()
            auth_login(request, user)
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
            return redirect(request.GET.get('next') or 'movies:index')
    else:
        loginform = AuthenticationForm()
    context = {
        'loginform': loginform,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    auth_logout(request)
    return redirect('movies:index')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        changeform = CustomUserChangeForm(instance=request.user, data=request.POST)
        if changeform.is_valid():
            changeform.save()
            return redirect('movies:index')
    else:
        changeform = CustomUserChangeForm(instance=request.user)
    context = {
        'changeform': changeform,
    }
    return render(request, 'accounts/update.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def pwchange(request):
    if request.method == 'POST':
        pwform = PasswordChangeForm(user=request.user, data=request.POST)
        if pwform.is_valid():
            pwform.save()
            update_session_auth_hash(request, request.user)
            return redirect('movies:index')
    else:
        pwform = PasswordChangeForm(user=request.user)
    context = {
        'pwform': pwform,
    }
    return render(request, 'accounts/pwchange.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('movies:index')