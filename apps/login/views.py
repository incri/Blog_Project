from django.contrib.auth.views import LoginView as _loginviews
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.views import LogoutView as _logoutviews

# login Views


class loginviews(_loginviews):
    template_name = 'login/login_page.html'
    success_url = reverse_lazy('home-page')


class RegisterViews(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('home-page')
    template_name = 'login/register.html'


class LogoutViews(_logoutviews):
    success_url = reverse_lazy('home-page')
