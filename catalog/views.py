from django.views.generic import ListView, DetailView
from catalog.models import Product
from catalog.mixins import ProductFilterMixin


class ProductListView(ListView):
    model = Product
    paginate_by = 15
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'



