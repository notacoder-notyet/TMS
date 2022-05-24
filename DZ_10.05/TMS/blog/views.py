from django import forms
from django.views.generic import DetailView, ListView, CreateView

from .models import Post


menu = ['Инфо', 'Добавить пост', 'Войти']


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'
    initial = {'menu':menu, 'title':'Главная страница'}


class PostVeiw(DetailView):
    model = Post
    template_name = 'blog/post_view.html'
    context = {'title':'Обзор поста'}


# class CreatePost(forms.Form):
#     model = Post
#     template_name = 'blog/create.html'

# def login():
    pass

# class RegisterUser(DataMixin, CreateView):
    pass
