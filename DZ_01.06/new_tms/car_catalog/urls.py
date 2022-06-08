from django.urls import path

from . import views

app_name = 'car_catalog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_brand/', views.add_brand ,name='add_brand'),
    path('add_model/', views.add_model ,name='add_model'),
    path('add_engine/', views.add_engine ,name='add_engine'),
]
