from .cart import Cart
from catalog.models import Product


def cart(request):
    return {'cart': Cart(request)}


def cart_detail(request):
    cart = Cart(request)
    cart_list_of_dict = []
    for item, value in cart.cart.items():
        product = Product.objects.get(id=item)
        if request.user.is_authenticated and request.user.is_from_portal:
            list_item = {
                'product': product,
                'price': product.price_with_discount,
                'quantity': value['quantity']
            }
        else:
            list_item = {
                'product': product,
                'price': value['price'],
                'quantity': value['quantity']
            }
        cart_list_of_dict.append(list_item)
    cart_sum = sum([float(x['price']) * float(x['quantity']) for x in cart_list_of_dict])
    return {
        'cart_list': cart_list_of_dict,
        'total_cart_sum': cart_sum
    }
