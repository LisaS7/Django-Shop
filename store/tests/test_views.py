from django.contrib.auth.models import User
from importlib import import_module
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse
from django.conf import settings

from store.models import Category, Product
from store.views import product_all


class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        User.objects.create(username='admin')
        Category.objects.create(name='blaster', slug='blaster')
        Product.objects.create(category_id=1, item='item test', created_by_id=1,
                               slug='item-test', price='20.00', image='blaster')

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts
        """
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='testdomain.com')
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
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = product_all(request)
        html = response.content.decode('utf-8')
        self.assertIn('<title>Rodian Arms - Home</title>', html)
