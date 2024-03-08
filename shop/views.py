from django.shortcuts import render
from django.views.generic.base import View
from .models import Product, Categories


class ShopView(View):
    """Products"""
    def get(self, request):
        products = Product.objects.all().order_by('-id')
        categories = Categories.objects.all().order_by('title')
        return render(request, 'shop.html', {'product_list': products, 'categories': categories})