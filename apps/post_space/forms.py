from django.forms import ModelForm

from apps.blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['author']
