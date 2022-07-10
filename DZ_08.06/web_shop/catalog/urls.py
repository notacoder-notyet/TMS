from django.urls import path, include
from rest_framework import routers

from catalog.views import CatalogViewSet

app_name = 'catalog'

router = routers.SimpleRouter()
router.register(r'catalog', CatalogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]