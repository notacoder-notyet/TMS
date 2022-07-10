from django.urls import path

from . import views

app_name = 'car_catalog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_brand/', views.CarBrandView.as_view() ,name='add_brand'),
    path('add_model/', views.CarModelView.as_view() ,name='add_model'),
    path('add_engine/', views.EngineView.as_view() ,name='add_engine'),
]
