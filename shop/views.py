from django.shortcuts import render

from django.views.generic import ListView, CreateView, TemplateView

from catalog.mixins import AjaxableResponseMixin
from catalog.models import Product
from .models import LogoWithPhones, DeliveryAndPayment, ExchangeAndReturn, HowToUse, Support, Contacts, AboutUs, \
    SocialNetwork, SliderMainPage


class HomePageView(TemplateView):
    template_name = 'shop/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['best_products'] = Product.objects.filter(is_best=True)
        context['new_products'] = Product.objects.order_by('-created')[:10]
        context['recommended_products'] = Product.objects.filter(is_recommended=True)
        context['slider_images'] = SliderMainPage.objects.all()
        context['logo_with_phones'] = LogoWithPhones.objects.first()
        context['social'] = SocialNetwork.objects.first()
        return context


class DeliveryAndPaymentView(TemplateView):

    template_name = 'shop/delivery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['deliveries'] = DeliveryAndPayment.objects.all()
        return context


class ExchangeAndReturnView(TemplateView):

    template_name = 'shop/'


class HowToUseView(TemplateView):

    template_name = 'shop/how-to-use.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['how_to_use_list'] = HowToUse.objects.all()
        return context


class SupportView(AjaxableResponseMixin, CreateView):

    model = Support
    fields = [
        'name',
        'email',
        'message'
    ]


class ContactsView(TemplateView):
    template_name = 'shop/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contacts.objects.first()
        context['social'] = SocialNetwork.objects.first()
        return context


class AboutUsView(TemplateView):
    template_name = 'shop/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutUs.objects.first()
        return context

