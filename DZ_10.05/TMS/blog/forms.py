from unicodedata import name
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import *


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='Username', widget=forms.TextInput(attrs={'class': 'form_input'}))
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form_input'}))


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        label='Username', widget=forms.TextInput(attrs={'class': 'form_input'}))
    email = forms.CharField(label='Email', widget=forms.TextInput(
        attrs={'class': 'form_input'}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput(attrs={'class': 'form_input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AddPostForm(forms.Form):
    name = forms.CharField(max_length=50)
    text = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # pub_date = forms.DateTimeField('date published')
    is_puplished = forms.BooleanField()
