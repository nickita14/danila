from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from sweet_shop.models import *


def shop(request):
    products = Product.objects.all()
    context = {
        'header' : 'Все наши товары',
        'products': products,
        'title': 'Магазин'
    }
    return render(request, 'sweet_shop/shop.html', context=context)


def show_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)

    context = {
        'product': product,
        'title': product.name,
    }

    return render(request, 'sweet_shop/product.html', context=context)


def show_category(request, category_slug):
    products = Product.objects.filter(categories__slug=category_slug)
    category = Category.objects.get(slug=category_slug)
    context = {
        'title': f'Категория - {category.name}',
        'header' : f'Товары в категори {category.name}',
        'products': products,
    }
    return render(request, 'sweet_shop/shop.html', context=context)
