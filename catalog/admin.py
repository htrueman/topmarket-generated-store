from django.contrib import admin
from catalog.models import Product, ProductImageURL


class ProductImageURLTabularInline(admin.TabularInline):
    model = ProductImageURL
    fields = (
        'product',
        'url'
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
        'price'
    )
    inlines = (ProductImageURLTabularInline, )


admin.site.register(Product, ProductAdmin)

