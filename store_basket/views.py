from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product

from .basket import Basket


def basket_summary(request):
    basket = Basket(request)
    return render(request, 'basket/summary.html', {'basket': basket})


# TODO: refactor add/delete/update to remove duplicate code
def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, quantity=product_quantity)

        basket_quantity = len(basket)
        response = JsonResponse({'quantity': basket_quantity})
        return response


def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basket_quantity = len(basket)
        basket_total = basket.get_total_price()
        response = JsonResponse({'quantity': basket_quantity, 'subtotal': basket_total})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        quantity = int(request.POST.get('quantity'))
        price = Product.products.get(id=product_id).price
        item_subtotal = quantity * price
        basket.update(product=product_id, quantity=quantity)

        basket_quantity = len(basket)
        basket_total = basket.get_total_price()
        response = JsonResponse({'quantity': basket_quantity, 'itemtotal': item_subtotal, 'subtotal': basket_total})
        return response
