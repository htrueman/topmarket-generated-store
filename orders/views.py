from django.http import JsonResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from basket.cart import Cart
from catalog.mixins import AjaxableResponseMixin
from .models import Order, OrderItem


class OrderView(TemplateView):
    template_name = 'orders/order.html'


class OrderCreateView(AjaxableResponseMixin, CreateView):
    # form_class = OrderForm
    model = Order
    fields = (
        'city',
        'first_name',
        'last_name',
        'patronymic',
        'email',
        'phone',
        'nova_poshta',
    )

    success_url = 'order/'

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            order = form.save()
            cart = Cart(self.request)
            OrderItem.objects.bulk_create([
                OrderItem(order=order, product=item['product'], quantity=item['quantity'])
                for item in cart
            ])
            return JsonResponse({
                'successed': True,
            })
        else:
            return response
