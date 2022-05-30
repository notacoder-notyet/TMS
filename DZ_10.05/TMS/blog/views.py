from django import forms
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView

from .models import Post
from .forms import *


class IndexView(ListView):
    model = Post
    template_name = 'blog/index.html'


class PostVeiw(DetailView):
    model = Post
    template_name = 'blog/post_view.html'



# class CreatePost(LoginRequiredMixin, forms.Form):
#     model = Post
#     template_name = 'blog/create.html'



class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'blog/login.html'

    def get_success_url(self) -> str:
        return reverse_lazy('blog:index')

def logout_user(request):
    logout(request)
    return redirect('blog:login')