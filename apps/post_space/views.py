from django.shortcuts import redirect, render
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from apps.blog.models import Post


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


class PostUpdateView(UpdateView):
    model = Post
    queryset = Post.objects.all()
    fields = ['content']
    template_name = 'post_space/update_form.html'
    success_url = '/home/'
