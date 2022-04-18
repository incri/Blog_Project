from django.shortcuts import render
from .models import Post


# from django.views.generic import ListView, FormView, CreateView
# from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(
        request,
        'blog/home.html',
        context={'posts': Post.objects.all()}
    )


"""
class PostList(LoginRequiredMixin, ListView):


    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
"""


'''class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    success_url = '/home/'
    form_class = PostForm
'''
