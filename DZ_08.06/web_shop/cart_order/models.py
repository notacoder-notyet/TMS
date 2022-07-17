from django.contrib.auth.models import User
from django.db import models

from catalog.models import Product
from .constants import STATUS


class Cart(models.Model):
    customer = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='carts')

    def __str__(self) -> str:
        return self.customer.username


class Order(models.Model):
    customer = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='orders')
    number = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=STATUS)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.number)