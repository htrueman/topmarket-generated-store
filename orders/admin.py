from django.contrib import admin
from .models import *


class OrderItemTabular(admin.TabularInline):
    model = OrderItem
    fields = (
        'product',
        'quantity',
    )
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (
        OrderItemTabular,
    )
    fields = (
        'city',
        'first_name',
        'last_name',
        'patronymic',
        'email',
        'phone',
        'nova_poshta',
    )
