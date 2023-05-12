from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import ProductCategory, Product, Basket
from django.core.paginator import Paginator


# Create your views here.


def index(request):
    context = {'title': 'Paradise for pets'}
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page_number=1):
    # products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    if category_id:
        products = Product.objects.filter(category_id=category_id)
        photos = False
    else:
        products = Product.objects.all()
        photos = True
    per_page = 6
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    context = {'title': 'Paradise for pets - Каталог',
               'categories': ProductCategory.objects.all(),
               'products': products_paginator,
               }
    if photos:
        return render(request, 'products/products.html', context)
    else:
        return render(request, 'products/products_no_photos.html', context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])