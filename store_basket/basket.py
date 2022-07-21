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

    def add(self, product, quantity):
        """
        Adding and updating the session basket data
        """
        product_id = product.id
        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'quantity': int(quantity)}

        self.session.modified = True
