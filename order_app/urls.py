from django.urls import path
from order_app.views import order_list_func, order_item_func, order_by_buyer, order_item_by_seller, order_item_by_product, order_by_code

urlpatterns = [
    path('orders_list', order_list_func),
    path('order_items', order_item_func),
    path('orders_buyer/<str:buyer_name>', order_by_buyer),
    path('order_items_seller/<str:seller_name>', order_item_by_seller),
    path('order_items_product/<str:product_name>',order_item_by_product),
    path('order_code/<str:code_input>', order_by_code)
]