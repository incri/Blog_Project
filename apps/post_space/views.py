from django.shortcuts import redirect, render
from .forms import PostForm
from django.contrib.auth.decorators import login_required


@login_required
def post_space(request):
    if request.method.lower() == 'get':
        form = PostForm()
        return render(request, 'post_space/post.html', {'form': form})
    else:
        post = PostForm(request.POST)
        if post.is_valid():
            post.save()
            return redirect('home-page')
