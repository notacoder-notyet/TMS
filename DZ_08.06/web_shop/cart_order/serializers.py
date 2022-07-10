from rest_framework import serializers

from .models import Cart, Order
from catalog.serializers import ProductSerializer

class CartSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # position = ProductSerializer(many=True)
    
    class Meta:
        model = Cart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # position = ProductSerializer(many=True)
    
    class Meta:
        model = Order
        fields = '__all__'