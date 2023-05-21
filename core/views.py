from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import views as auth_views, logout

from CustomerIntegrityManagementSystem import settings
from .forms import LoginForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'auth/login.html'


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect(settings.LOGOUT_REDIRECT_URL)


def index(request):
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        return render(request, 'index.html', {})


@login_required
def profile(request):
    return render(request, 'profile.html', {})
