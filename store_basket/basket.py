from decimal import Decimal

from django.conf import settings

from store.models import Product


class Basket:
    """
    A base basket class providing default behaviours to be inherited or overriden as necessary.
    """

    def __init__(self, request) -> None:
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if settings.BASKET_SESSION_ID not in self.session:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    def __len__(self):
        """
        Get basket data and count the number of items
        """
        return sum(item['quantity'] for item in self.basket.values())

    def __iter__(self):
        """
        Collect the product_id from the session data to query the database and return products
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def add(self, product: int, quantity: int) -> None:
        """
        Adding and updating the session basket data
        """
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['quantity'] = quantity
        else:
            self.basket[product_id] = {'price': str(product.price), 'quantity': int(quantity)}

        self.save()

    def delete(self, product: int) -> None:
        """
        Delete item from basket session data
        """
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def update(self, product: int, quantity: int) -> None:
        """
        Update quantity in basket session data
        """
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['quantity'] = quantity
            self.save()

    def save(self) -> None:
        self.session.modified = True

    def clear(self) -> None:
        """
        Remove basket from session
        """
        del self.session[settings.BASKET_SESSION_ID]
        self.save()

    def get_subtotal_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

    def get_total_price(self) -> Decimal:

        subtotal = sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(30)

        total = subtotal + Decimal(shipping)
        return total
