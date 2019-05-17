from django.views.generic import ListView, DetailView
from catalog.models import Product
from catalog.mixins import ProductFilterMixin


class ProductListView(ListView, ProductFilterMixin):
    model = Product
    paginate_by = 15
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductListByCategoryView(ListView, ProductFilterMixin):
    model = Product
    paginate_by = 15
    template_name = 'catalog/product_list_by_category.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id', None)
        queryset = queryset.filter(category_id=category_id)
        return queryset


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
    context_object_name = 'product'
