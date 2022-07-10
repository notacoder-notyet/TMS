from django.db import models

from .constants import PRODUCTS_TYPE, QUALITY

class Brand(models.Model):
    name = models.CharField(max_length=50)
    quality = models.CharField(max_length=50, choices=QUALITY)
    products_type = models.CharField(max_length=50, choices=PRODUCTS_TYPE)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    cost = models.PositiveIntegerField()
    availability = models.BooleanField()
    photo = models.FileField(upload_to='uploads/photo_models', null=True, blank=True)

    def __str__(self):
        return self.name