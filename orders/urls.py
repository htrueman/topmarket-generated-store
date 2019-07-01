from django.urls import path

from .views import OrderCreateView, OrderView

app_name='orders'

urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    # path('order_item/', OrderItemCreateView.as_view(), name='order_item'),
]