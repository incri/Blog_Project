from django.contrib.auth.views import LoginView as _loginviews


class loginviews(_loginviews):
    template_name = 'login/login_page.html'
