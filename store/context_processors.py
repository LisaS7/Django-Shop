from .models import Category


def categories(request) -> dict:
    return {
        'categories': Category.objects.all()
    }
