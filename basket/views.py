from django.shortcuts import render

from django.shortcuts import get_object_or_404
from catalog.models import Product
from .cart import Cart
from django.http import HttpResponse
import json


def cart_add(request):
    cart = Cart(request)
    product_id = request.GET.get('product_id', None)
    product = Product.objects.get(id=product_id)
    response_data = {}
    try:
        cart.add(product=product)
        response_data['added'] = True
        response_data['message'] = 'Товар успешно добавлен в корзину'
    except:
        response_data['added'] = False
        response_data['message'] = "Ошибка. Не удалось добавить в корзину."

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def cart_remove(request):
    product_id = request.GET.get('product_id', None)
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    response_data = {}
    try:
        cart.remove(product)
        response_data['deleted'] = True
    except:
        response_data['deleted'] = False
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def cart_change_quantity(request):
    cart = Cart(request)
    product_id = request.GET.get('product_id', None)
    product = Product.objects.get(id=product_id)
    response_data = {}
    if request.GET.get('quantity'):
        quantity = request.GET.get('quantity')
        try:
            cart.set_quantity(product=product, quantity=quantity)
            response_data['changed'] = True
        except:
            response_data['changed'] = False
    else:
        response_data['changed'] = False
    return HttpResponse(json.dumps(response_data), content_type="application/json")

