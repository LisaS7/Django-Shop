from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from store.models import Product

from .basket import Basket


def basket_summary(request):
    return render(request, 'store/basket/summary.html')


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_quantity = int(request.POST.get('quantity'))
        product = get_object_or_404(Product, id=product_id)
        
        basket.add(product=product, quantity=product_quantity)
        response = JsonResponse({'test': 'data'})
        return response
