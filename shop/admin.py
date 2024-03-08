from django.contrib import admin
from .models import Product, Categories


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(Categories)
class CategoryAdmin(admin.ModelAdmin):
    pass