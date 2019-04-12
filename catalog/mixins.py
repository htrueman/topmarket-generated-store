from django.http import JsonResponse
from django.db.models import Q


class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.is_ajax():
            form.save()
            return JsonResponse({
                'successed': True,
            })
        else:
            return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if self.request.is_ajax():
            form_errors = {}
            errors = {}
            for key, value in form.errors.items():
                errors[key] = ' '.join(value)
            form_errors['errors'] = errors
            return JsonResponse(form_errors)
        else:
            return response


class ProductFilterMixin:
    def get_queryset(self):
        queryset = self.model.objects.all()
        if self.request.GET.get('order'):
            order_filter = self.request.GET.get('order')
            queryset = queryset.order_by(order_filter)
        if self.request.GET.get('min_price'):
            price_min_filter = self.request.GET.get('min_price')
            queryset = queryset.filter(price__gte=price_min_filter)
        if self.request.GET.get('max_price'):
            price_max_filter = self.request.GET.get('max_price')
            queryset = queryset.filter(price__lte=price_max_filter)
        if len(self.request.GET.getlist('brand')) > 0:
            brand_list = self.request.GET.getlist('brand')
            queryset = queryset.filter(brand__in=brand_list)
        if self.request.GET.get('q'):
            q = self.request.GET.get('q')
            queryset = queryset.filter(Q(name__icontains=q) or Q(description__icontains=q))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        data = super().get_context_data(**kwargs)
        products = self.get_queryset()
        # data['brands'] = Brand.objects.filter(id__in=products.values_list('brand'))
        data['category_slug'] = self.kwargs['slug']
        data['category_pk'] = self.kwargs['pk']
        return data
