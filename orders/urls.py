from django.urls import path

from .views import OrderCreateView, OrderItemCreateView

urlpatterns = [
    path('order/', OrderCreateView.as_view, name='order'),
    path('order_item/', OrderItemCreateView.as_view, name='order_item')


]
