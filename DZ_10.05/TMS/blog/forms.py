from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import *
from users.models import CustomUser
from users.forms import CustomUserCreationForm


class LoginUserForm(AuthenticationForm):
    email = forms.EmailField(
        label='Email', 
        widget=forms.TextInput(attrs={'class': 'form_input'}))
    password = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={'class': 'form_input'}))

    class Meta:
        model = CustomUser
        fields = ('email', 'password')


class RegisterUserForm(CustomUserCreationForm):
    username = forms.CharField(
        label='Username', 
        widget=forms.TextInput(attrs={'class': 'form_input'}))
    email = forms.CharField(
        label='Email', 
        widget=forms.TextInput(attrs={'class': 'form_input'}))
    password1 = forms.CharField(
        label='Password', 
        widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    password2 = forms.CharField(
        label='Password confirmation', 
        widget=forms.PasswordInput(attrs={'class': 'form_input'}))

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')


class CreatePostForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    text = forms.CharField(required=True, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # pub_date = forms.DateTimeField('date published')

