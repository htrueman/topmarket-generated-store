from django.shortcuts import render

from django.views.generic import  ListView, CreateView

from catalog.mixins import AjaxableResponseMixin
from .models import LogoWithPhones, DeliveryAndPayment, ExchangeAndReturn, HowToUse, Support, Contacts, AboutUs, \
    SocialNetwork


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


