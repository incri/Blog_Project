from django.urls import path
from .blog import views

urlpatterns = [
    path('home/', views.home, name="home-page"),
    # path('posts/', views.PostList.as_view(), name='post-list')
    path('post/', views.post_create),
    path('create/', views.PostCreateView.as_view())
]
