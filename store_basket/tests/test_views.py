from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='blaster', slug='blaster')
        Product.objects.create(
            category_id=1, item='item test', created_by_id=1, slug='item-test', price='20.00', image='blaster'
            )
        Product.objects.create(
            category_id=1, item='item test', created_by_id=1, slug='item-test', price='20.00', image='blaster'
            )
        Product.objects.create(
            category_id=1, item='item test', created_by_id=1, slug='item-test', price='20.00', image='blaster'
            )

        self.client.post(
            reverse('store_basket:basket_add'), {'productid': 1, 'quantity': 1, 'action': 'post'}, xhr=True
        )
        self.client.post(
            reverse('store_basket:basket_add'), {'productid': 2, 'quantity': 2, 'action': 'post'}, xhr=True
        )

    def test_basket_url(self):
        """
        Test basket summary response status
        """
        response = self.client.get(reverse('store_basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """
        Test adding items to basket
        """

        response = self.client.post(
            reverse('store_basket:basket_add'), {'productid': 3, 'quantity': 1, 'action': 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'quantity': 4})

        response = self.client.post(
            reverse('store_basket:basket_add'), {'productid': 2, 'quantity': 1, 'action': 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'quantity': 3})

    def test_basket_delete(self):
        """
        Test deleting items from basket
        """
        response = self.client.post(
            reverse('store_basket:basket_delete'), {'productid': 2, 'action': 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'quantity': 1, 'subtotal': '20.00'})

    def test_basket_update(self):
        """
        Test updating items in basket
        """
        response = self.client.post(
            reverse('store_basket:basket_update'), {'productid': 2, 'quantity': 1, 'action': 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'quantity': 2, 'itemtotal': '20.00', 'subtotal': '40.00'})
