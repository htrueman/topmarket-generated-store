from django.shortcuts import render

from django.views.generic import DetailView, ListView, CreateView

from shop.mixins import AjaxableResponseMixin
from .models import LogoWithPhones, DeliveryAndPayment, ExchangeAndReturn, HowToUse, Support, Contacts, AboutUs, \
    SocialNetwork


class LogoWithPhonesView(DetailView):

    model = LogoWithPhones


class SocialNetworkView(DetailView):

    model = SocialNetwork


class DeliveryAndPaymentView(ListView):

    model = DeliveryAndPayment


class ExchangeAndReturnView(DetailView):

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


class ContactsView(DetailView):

    model = Contacts


class AboutUsView(DetailView):

    model = AboutUs
