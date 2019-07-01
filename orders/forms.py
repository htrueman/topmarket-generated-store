from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'city',
            'first_name',
            'last_name',
            'patronymic',
            'email',
            'phone',
            'nova_poshta',
        )
