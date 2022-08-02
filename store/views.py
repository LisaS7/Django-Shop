from django.shortcuts import get_object_or_404, render

from .models import Category, Product


def home(request):
    return render(request, 'store/index.html')


def contact(request):
    return render(request, 'store/contact.html')


def category_list(request, category_slug: str):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})


def product_all(request):
    products = Product.products.all()
    return render(request, 'store/all.html', {'products': products})


def product_detail(request, slug: str):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/single.html', {'product': product})
