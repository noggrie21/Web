from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, CustomUserChangeform
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
        
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
    if request.user.is_authenticated:
        return redirect('articles:indes')

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


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        changeform = CustomUserChangeform(request.POST, instance=request.user)
        if changeform.is_valid():
            changeform.save()
            return redirect('movies:index')
    else:
        changeform = CustomUserChangeform(instance=request.user)
    context = {
        'changeform':changeform,
    }
    return render(request, 'accounts/update.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    return redirect('movies:index')


@login_required
@require_http_methods(['GET', 'POST'])
def password(request):
    if request.method == 'POST':
        changeform = PasswordChangeForm(request.user, request.POST)
        if changeform.is_valid():
            changeform.save()
            update_session_auth_hash(request, changeform.user)
            return redirect('movies:index')
    else:
        changeform = PasswordChangeForm(request.user)
    context = {
        'changeform':changeform,
    }
    return render(request, 'accounts/change_password.html', context)