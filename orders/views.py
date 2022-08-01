from django.shortcuts import render
from django.http.response import JsonResponse

from store_basket.basket import Basket
from .models import Order, OrderItem


def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        user_id = request.user.id
        order_key = request.POST.get('order_key')
        basket_total = basket.get_total_price()

        if Order.objects.filter(order_key=order_key).exists():
            pass
        else:
            name = request.POST.get('name')
            address = request.POST.get('address')
            city = request.POST.get('city')
            planet = request.POST.get('planet')

            order = Order.objects.create(
                user_id=user_id, full_name=name, address=address,
                city=city, planet=planet,
                total_paid=basket_total, order_key=order_key
                )
            order_id = order.pk
            for item in basket:
                OrderItem.objects.create(
                    order_id=order_id, product=item['product'],
                    price=item['price'], quantity=item['quantity']
                )
            response = JsonResponse({'success': 'Order added to database'})
        return response
