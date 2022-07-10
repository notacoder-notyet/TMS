from rest_framework import viewsets

from .models import Product, Brand
from .serializers import BrandSerializer, ProductSerializer
from .permissions import IsAdminOrReadOnly


class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )

