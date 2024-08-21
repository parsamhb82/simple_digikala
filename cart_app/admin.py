from django.contrib.admin import register, ModelAdmin
from cart_app.models import Cart, Cart_item

@register(Cart)
class CartAdmin(ModelAdmin):
    list_display = [
        'buyer',
        'code'
    ]
    search_fields = [
        'buyer',
    ]
@register(Cart_item)
class Cart_timeadmin(ModelAdmin):
    list_display = [
        'cart',
        'seller',
        'product',
        'num'
    ]
    search_fields = [
        'cart',
        'seller',
        'product'
    ]
