from .models import Category
from django.conf import settings


def categories(request) -> dict:
    return {
        'categories': Category.objects.all()
    }


def currency(request) -> dict:
    return {
        'default_currency': settings.DEFAULT_CURRENCY
    }
