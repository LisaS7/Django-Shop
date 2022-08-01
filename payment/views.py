from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from store_basket.basket import Basket


@login_required
def BasketView(request):
    basket = Basket(request)
    total = basket.get_total_price()

    client_payment = {'payment_method': 0}

    return render(request, 'payment/main.html', client_payment)


def order_placed(request):
    # basket = Basket(request)
    # basket.clear()
    return render(request, 'payment/orderplaced.html')
