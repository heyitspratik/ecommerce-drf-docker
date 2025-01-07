from django.contrib import admin
from .models import Product, Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'description',]
    list_per_page = 10

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # list_display = ['id', 'products', 'status',]
    list_per_page = 10