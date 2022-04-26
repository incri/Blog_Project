from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .forms import PostForm
from apps.blog.models import Post


@login_required
def post_space(request):
    if request.method.lower() == 'get':
        form = PostForm()
        return render(request, 'post_space/post.html', {'form': form})
    else:
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home-page')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['content']
    template_name = 'post_space/update_form.html'
    success_url = '/home/'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_space/delete.html'
    success_url = '/home/'
