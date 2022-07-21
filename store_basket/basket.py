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
