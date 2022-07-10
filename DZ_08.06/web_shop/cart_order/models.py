from django.contrib.auth.models import User
from django.db import models

from catalog.models import Product
from .constants import STATUS


class Cart(models.Model):
    customer = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    position = models.ManyToManyField(Product, related_name='item')

    def __str__(self) -> str:
        return self.customer.username


class Order(models.Model):
    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    position = models.ManyToManyField(Product, related_name='items')
    number = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=STATUS)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.number)