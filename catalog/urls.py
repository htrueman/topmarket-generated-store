from django.urls import path
from .views import *

app_name = 'catalog'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='products_list'),
    path('products/category/<int:category_id>', ProductListByCategoryView.as_view(), name='products_by_category'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]