from django.urls import path

from .views import DeliveryAndPaymentView, ExchangeAndReturnView, HowToUseView, \
    SupportView, ContactsView, AboutUsView, HomePageView

app_name = 'shop'


urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('delivery_and_payment/', DeliveryAndPaymentView.as_view(), name='delivery_and_payment_url'),
    path('exchange_and_return/', ExchangeAndReturnView.as_view(), name='exchange_and_return_url'),
    path('how_to_use/', HowToUseView.as_view(), name='how_to_use_url'),
    path('support/', SupportView.as_view(), name='support_url'),
    path('contacts/', ContactsView.as_view(), name='contacts_url'),
    path('about_us/', AboutUsView.as_view(), name='about_us_url')
]
