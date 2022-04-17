from django.shortcuts import redirect, render

from apps.blog.forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, FormView, CreateView
# from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(
        request,
        'blog/home.html',
        context={'posts': Post.objects.all()}
    )


def post_create(request):
    if request.method.lower() == 'get':
        return render(request, 'blog/post_create.html', {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home-page')

"""
class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
"""


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    success_url = '/home/'
    form_class = PostForm
