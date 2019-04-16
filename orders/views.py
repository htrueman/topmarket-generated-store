from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from .models import Order, OrderItem


class OrderCreateView(CreateView):
    model = Order


class OrderItemCreateView(CreateView):
    model = OrderItem
