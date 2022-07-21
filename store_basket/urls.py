from django.urls import path

from . import views

urlpattern = [
    path('', views.basket_summary, name='basket_summary'),
]