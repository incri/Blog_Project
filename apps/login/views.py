from django.contrib.auth.views import LoginView as _loginviews
from django.forms import ValidationError
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.views import LogoutView as _logoutviews
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# login Views


class loginviews(_loginviews):
    template_name = 'login/login_page.html'
    success_url = reverse_lazy('home-page')

    def form_valid(self, form):
        user = form.get_user()
        user_activity = user.activity
        if (
            user_activity.login_attempts >= 3
            and user_activity.can_login_at > timezone.now()
        ):
            raise ValidationError("Max attemp reached")
        user_activity.login_attempts = 0
        user_activity.can_login_at = None
        user_activity.save()
        return super().form_valid(form)


class RegisterViews(CreateView):
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('home-page')
    template_name = 'login/register.html'


class LogoutViews(_logoutviews):
    success_url = reverse_lazy('home-page')


@login_required 
def profile(request):
    return (request, 'profile.html')
