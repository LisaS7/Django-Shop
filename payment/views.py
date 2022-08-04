from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from store_basket.basket import Basket


@login_required
def BasketView(request):
    return render(request, 'payment/payment_form.html')


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')
