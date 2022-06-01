from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostVeiw.as_view(), name='post_view'),
    path('author/<int:pk>/', views.AuthorView.as_view(), name='author_view'),
    path('post/create-post/', views.create_post ,name='create_post'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.RegisterUser.as_view(), name='register'),
]
