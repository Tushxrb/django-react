from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'photo']

admin.site.register(Product, ProductAdmin)

