from django.contrib import admin

from .models import Cart, Order


class CartAdmin(admin.ModelAdmin):
    list_display = ('customer',)
    search_fields = ('customer',)


class OrderAdmin(admin.ModelAdmin):
    search_fields = ('number', 'customer')


admin.site.register(Cart, CartAdmin)
admin.site.register(Order, OrderAdmin)
