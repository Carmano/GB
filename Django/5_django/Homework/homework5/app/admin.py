from django.contrib import admin
from .models import Product, Client, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'count', 'date_added', 'image')
    ordering = ('-name',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'address', 'date_registered')
    ordering = ('-date_registered',)
    list_filter = ('name',)
    search_fields = ('name',)
    search_help_text = 'Name of the client'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('get_product_name', 'get_client_name', 'date_ordered', 'total_price')
