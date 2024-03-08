from django.shortcuts import render
from django.views.generic.base import View
from .models import About
from shop.models import Product, Categories


class AboutView(View):
    """About View"""

    def get(self, request):
        about = About.objects.all()
        return render(request, 'about.html', {'about': about})


class IndexView(View):
    """Index View"""

    def get(self, request):
        products = Product.objects.all().order_by('-id')
        category = Categories.objects.all()
        return render(request, 'index.html', {'product_list': products, 'product_categories': category})
