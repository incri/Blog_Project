from django.urls import path
from .blog import views
from .post_space import views as _views

urlpatterns = [
    path('home/', views.home, name="home-page"),
    # path('posts/', views.PostList.as_view(), name='post-list')
    path('post/', _views.post_space),
    # path('create/', views.PostCreateView.as_view())
]
