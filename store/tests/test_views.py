from unittest import skip
from django.test import TestCase, Client, RequestFactory
from django.http import HttpRequest
from django.urls import reverse
from django.contrib.auth.models import User
from store.models import Category, Product
from store.views import all_products

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        User.objects.create(username='admin')
        Category.objects.create(name='blaster', slug='blaster')
        Product.objects.create(category_id=1, item='item test', created_by_id=1,
                                slug='item-test', price='20.00', image='blaster')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test product detail response status
        """
        response = self.c.get(reverse('store:product_detail', args=['item-test']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test category detail response status
        """
        response = self.c.get(reverse('store:category_list', args=['blaster']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """
        Test homepage html contents
        """
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>Rodian Arms - Home</title>', html)

    def test_view_function(self):
        """
        Trying out the RequestFactory
        """
        request = self.factory.get('/item/item-test')
        response = all_products(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>Rodian Arms - Home</title>', html)