"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.login.views import loginviews
from apps.post_space.views import PostDeleteView, PostUpdateView
from apps.login.views import RegisterViews
from apps.login.views import LogoutViews
from apps.user.views import ProfileViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls')),
    path('accounts/login/', loginviews.as_view(), name='login-page'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('resister/', RegisterViews.as_view(), name='resister'),
    path('accounts/logout/', LogoutViews.as_view(), name='logout-page'),
    path('accounts/profile/', ProfileViews, name='profile-page'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
