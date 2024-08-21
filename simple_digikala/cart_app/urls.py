from django.urls import path
from cart_app.views import cart_item_func, cart_list_func,cart_item_by_seller, cart_by_buyer, cart_by_code, cart_item_by_product

urlpatterns = [
    path('carts_list', cart_list_func),
    path('cart_items_list', cart_item_func),
    path('carts_list/by_seller/<str:seller_name>',cart_item_by_seller),
    path('carts_list/by_buyer/<str:buyer_name>',cart_by_buyer),
    path('cart_item_by_product/<product_name>', cart_item_by_product),
    path('cart_by_code/<code_input>', cart_by_code)

]