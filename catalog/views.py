from django.views.generic import ListView, DetailView
from catalog.models import Product, ProductCharacteristic
from catalog.mixins import ProductFilterMixin


class ProductListView(ProductFilterMixin, ListView):
    model = Product
    paginate_by = 15
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'


class ProductListByCategoryView(ProductFilterMixin, ListView):
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_characteristics'] = ProductCharacteristic.objects.filter(
            product_id=self.kwargs['pk']).order_by('characteristic_type')
        return context
