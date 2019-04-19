from rest_framework.generics import UpdateAPIView, ListCreateAPIView, RetrieveUpdateAPIView

from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import *
from shop.models import *


class MyStoreDomainNameUpdateView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = MyStore

    def update(self, request, pk=1, *args, **kwargs):
        result = super().update(request, *args, **kwargs)
        return result

    def get_object(self):
        domain, _ = MyStore.objects.get_or_create(
            id=1
        )
        return domain


class MyStoreInfoHeaderFooterUpdateView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = MyStoreInfoHeaderFooterSerializer

    def update(self, request, pk=1, *args, **kwargs):
        result = super().update(request, *args, **kwargs)
        return result

    def get_object(self):
        header, _ = MyStore.objects.get_or_create(
            id=1
        )
        return header


class MyStoreSliderUpdateView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = MyStore

    def update(self, request, pk=1, *args, **kwargs):
        result = super().update(request, *args, **kwargs)
        return result

    def get_object(self):
        slider, _ = MyStore.objects.get_or_create(
            id=1
        )
        return slider


class LogoWithPhonesUpdateView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = LogoWithPhonesSerializer

    def update(self, request, pk=1, *args, **kwargs):
        result = super().update(request, *args, **kwargs)
        return result

    def get_object(self):
        logo, _ = LogoWithPhones.objects.get_or_create(
            id=1
        )
        return logo


class SocialNetworkUpdateView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = SocialNetworksSerializer

    def update(self, request, pk=1, *args, **kwargs):
        result = super().update(request, *args, **kwargs)
        return result

    def get_object(self):
        social, _ = SocialNetwork.objects.get_or_create(
            id=1
        )
        return social


class DeliveryAndPaymentUpdateView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = DeliveryAndPaymentSerializer

    def update(self, request, pk=1, *args, **kwargs):
        result = super().update(request, *args, **kwargs)
        return result

    def get_object(self):
        delivery, _ = DeliveryAndPayment.objects.get_or_create(
            id=1
        )
        return delivery


class ExchangeAndReturnUpdateView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = ExchangeAndReturnSerializer

    def update(self, request, pk=1, *args, **kwargs):
        result = super().update(request, *args, **kwargs)
        return result

    def get_object(self):
        exchange, _ = ExchangeAndReturn.objects.get_or_create(
            id=1
        )
        return exchange


class HowToUseUpdateView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = HowToUseSerializer

    def update(self, request, pk=1, *args, **kwargs):
        result = super().update(request, *args, **kwargs)
        return result

    def get_object(self):
        use, _ = ExchangeAndReturn.objects.get_or_create(
            id=1
        )
        return use


class ContactsUpdateView(UpdateAPIView):
    permission_classes = [AllowAny, ]
    serializer_class = ContactsSerializer

    def update(self, request, pk=1, *args, **kwargs):
        result = super().update(request, *args, **kwargs)
        return result

    def get_object(self):
        contact, _ = ExchangeAndReturn.objects.get_or_create(
            id=1
        )
        return contact


class AboutUsUpdateView(RetrieveUpdateAPIView):
    model = AboutUs
    permission_classes = [AllowAny, ]
    serializer_class = AboutUsSerializer

    def update(self, request, pk=1, *args, **kwargs):
        result = super().update(request, *args, **kwargs)
        print(request.data)
        return result

    def get_object(self):
        about, _ = AboutUs.objects.get_or_create(
            id=1
        )
        return about




