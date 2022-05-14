from django.views.generic import ListView, DetailView
from django import forms

from .models import Post


class IndexView(ListView):
    model = Post
    template_name = 'index.html'


class PostVeiw(DetailView):
    model = Post
    template_name = 'post_view.html'


# class CreatePost(forms.Form):
#     model = Post
#     template_name = 'create.html'