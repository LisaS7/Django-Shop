from store.models import Product
from decimal import Decimal


class Basket:
    """
    A base basket class providing default behaviours to be inherited or overriden as necessary.
    """

    def __init__(self, request) -> None:
        self.session = request.session
        basket = self.session.get('session-key')
        if 'session-key' not in self.session:
            basket = self.session['session-key'] = {}
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

    def add(self, product, quantity):
        """
        Adding and updating the session basket data
        """
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['quantity'] = quantity
        else:
            self.basket[product_id] = {'price': str(product.price), 'quantity': int(quantity)}

        self.save()

    def delete(self, product):
        """
        Delete item from basket session data
        """
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def update(self, product, quantity):
        """
        Update quantity in basket session data
        """
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['quantity'] = quantity
            self.save()

    def save(self):
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())
