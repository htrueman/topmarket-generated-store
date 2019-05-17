from django.contrib import admin
from catalog.models import *
from mptt.admin import MPTTModelAdmin


class ProductImageURLTabularInline(admin.TabularInline):
    model = ProductImageURL
    fields = (
        'product',
        'url'
    )
    extra = 0


class ProductCharacteristicTabularInline(admin.TabularInline):
    model = ProductCharacteristic
    fields = (
        'product',
        'characteristic_type',
        'name',
        'value'
    )
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    fields = (
        'id',
        'category',
        'availability',
        'name',
        'vendor_code',
        'product_type',
        'brand',
        'count',
        'description',
        'price',
        'is_best',
        'is_recommended',
    )
    inlines = (ProductImageURLTabularInline, ProductCharacteristicTabularInline, )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(FeedBack)
