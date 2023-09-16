from django.contrib import admin
from .models import Product, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    list_filter = ('name', 'price',)
    search_fields = ('name', 'price',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'address', 'display_products_ordered', 'total_price',)
    list_filter = ('customer', 'total_price',)
    search_fields = ('customer__username', 'address',)

    def display_products_ordered(self, obj):
        products = [item.product.name for item in obj.orderitem_set.all()]
        return ", ".join(products)

    display_products_ordered.short_description = 'Products Ordered'

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity',)
    list_filter = ('order', 'product', 'quantity',)
    search_fields = ('order__customer__username', 'product__name',)

