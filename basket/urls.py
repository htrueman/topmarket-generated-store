from django.urls import path

from .views import cart_add, cart_remove, cart_change_quantity

app_name = 'basket'

urlpatterns = [
    path('remove/', cart_remove, name='cart_remove'),
    path('add/', cart_add, name='cart_add'),
    path('change_quantity/', cart_change_quantity, name='cart_change_quantity'),
]