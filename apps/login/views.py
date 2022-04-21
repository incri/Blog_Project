from django.contrib.auth.views import LoginView as _loginviews
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import RegisterForm

# login Views


class loginviews(_loginviews):
    template_name = 'login/login_page.html'


class RegisterViews(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('home-page')
    template_name = 'login/register.html'
