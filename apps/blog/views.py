from django.shortcuts import render
from .models import Post


def home(request):

    data = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context= data)
