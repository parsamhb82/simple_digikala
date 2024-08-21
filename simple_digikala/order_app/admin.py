from django.contrib.admin import register, ModelAdmin

from order_app.models import Order, Order_item

@register(Order)
class Orderadmin(ModelAdmin):
    list_display = [
        'buyer',
        'code'
    ]
    search_fields = [
        'buyer',
        'code'
    ]

@register(Order_item)
class Order_itemadmin(ModelAdmin):
    list_display = [
        'order',
        'seller',
        'product',
        'num'
    ]
    search_fields = [
        'order',
        'seller',
        'product'
    ]