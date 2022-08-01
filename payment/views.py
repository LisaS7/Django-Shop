from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def BasketView(request):
    return render(request, 'payment/main.html')

