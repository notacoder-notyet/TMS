from django.http import request
from django.contrib.auth.models import User
from rest_framework import viewsets, response, status
from rest_framework.decorators import action

from .models import Cart, Order
from .serializers import CartSerializer, OrderSerializer
from .permissions import IsOwnerOrReadOnly


class CartViewSet(viewsets.ModelViewSet):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_queryset(self):
        return self.get_queryset().filter(user=self.request.user)
    


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    @action(
        detail=False,
        methods=['post'],
        url_path='create',
    )
    def create_order(self,request):
        cart = request.user.cart
        order = Order.objects.create(user=request.user)
        order.items.set(cart.items.all)

        cart.items.clear()

        serializer = self.get_serializer(order)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)


