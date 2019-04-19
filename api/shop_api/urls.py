from django.urls import path
from .views import *

app_name = 'api_shop'

urlpatterns = [
    path('domain_name/', MyStoreDomainNameUpdateView.as_view(), name='domain_name_update'),
    path('header_footer_info', MyStoreInfoHeaderFooterUpdateView.as_view(), name='header_footer_inf0_update'),
    path('slider/', MyStoreSliderUpdateView.as_view(), name='slider_update'),
    path('logo_with_phones', LogoWithPhonesUpdateView.as_view(), name='logo_with_phones_update'),
    path('networks/', SocialNetworkUpdateView.as_view(), name='networks_update'),
    path('delivery_payment', DeliveryAndPaymentUpdateView.as_view(), name='delivery_payment_update'),
    path('exchange_return', ExchangeAndReturnUpdateView.as_view(), name='exchange_return_update'),
    path('how_to_use', HowToUseUpdateView.as_view(), name='how_to_use_update'),
    path('contacts/', ContactsUpdateView.as_view(), name='contacts_update'),
    path('about_us/', AboutUsUpdateView.as_view(), name='about_us_update')
]