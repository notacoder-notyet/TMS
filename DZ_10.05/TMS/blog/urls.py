from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostVeiw.as_view(), name='post_view'),
    # path('post/create/'), views. ,name='create'),
]
