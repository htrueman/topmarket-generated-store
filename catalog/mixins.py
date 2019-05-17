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
        queryset = super().get_queryset()
        brands = self.request.GET.getlist('brand', None)
        price_min = self.request.GET.get('min_price', None)
        price_max = self.request.GET.get('max_price', None)
        print(price_min, price_max)
        if brands:
            queryset = queryset.filter(brand__in=brands)
        if price_min:
            queryset = queryset.filter(price__gte=price_min)
        if price_max:
            queryset = queryset.filter(price__lte=price_max)
        print(queryset)
        return queryset

    def get_context_data(self, *args, **kwargs):
        # context = super().get_context_data(*args, **kwargs)
        context = {}
        min_price = self.request.GET.get('min_price', '')
        max_price = self.request.GET.get('max_price', '')
        context['brands'] = self.request.GET.getlist('brand', [])
        context['min_price'] = min_price
        context['max_price'] = max_price
        context['brand_list'] = self.model.objects.all().distinct('brand').values_list('brand', flat=True)
        context['join_brand'] = ''.join(['&brand=' + brand for brand in self.request.GET.getlist('brand', [])])
        context['min_price_join'] = '&min_price=' + min_price if min_price else ''
        context['max_price_join'] = '&max_price=' + max_price if max_price else ''
        return context
