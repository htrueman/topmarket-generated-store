from django.shortcuts import render

from django.views.generic import ListView, CreateView, TemplateView

from catalog.mixins import AjaxableResponseMixin
from catalog.models import Product
from .models import LogoWithPhones, DeliveryAndPayment, ExchangeAndReturn, HowToUse, Support, Contacts, AboutUs, \
    SocialNetwork


class HomePageView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['best_products'] = Product.objects.filter(is_best=True)
        context['new_products'] = Product.objects.order_by('-created')[:10]
        context['recommended_products'] = Product.objects.filter(is_recommended=True)
        return context


class LogoWithPhonesView(ListView):

    model = LogoWithPhones


class SocialNetworkView(ListView):

    model = SocialNetwork


class DeliveryAndPaymentView(ListView):

    model = DeliveryAndPayment


class ExchangeAndReturnView(ListView):

    model = ExchangeAndReturn


class HowToUseView(ListView):

    model = HowToUse


class SupportView(AjaxableResponseMixin, CreateView):

    model = Support
    fields = [
        'name',
        'email',
        'message'
    ]


class ContactsView(ListView):

    model = Contacts


class AboutUsView(ListView):

    model = AboutUs


