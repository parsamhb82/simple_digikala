from django.http.response import JsonResponse
from order_app.models import Order, Order_item

def order_list_func(request):
    orders = Order.objects.all()
    orders_list = []
    for order in orders:
        order : Order
        order_dict = {
            'buyer' : order.buyer.name,
            'date' : order.date,
            'code' : order.code,
            'cart_code' : order.cart.code,
            'bill' : order.bill
        }
        orders_list.append(order_dict)
    return JsonResponse(orders_list,safe=False)

def order_item_func(request):
    order_items = Order_item.objects.all()
    order_items_list = []
    for order_item in order_items:
        order_item : Order_item
        order_item_dict = {
            'order_code' : order_item.order.code,
            'buyer' : order_item.order.buyer.name,
            'seller' : order_item.seller.name,
            'product' : order_item.product.name,
            'bill' : order_item.price
        }
        order_items_list.append(order_item_dict)
    return JsonResponse(order_items_list, safe=False)

def order_by_buyer(request, buyer_name):
    try:
        orders = Order.objects.filter(buyer__name = buyer_name)
        orders_list = []
        for order in orders:
            order : Order
            order_dict = {
                'buyer' : order.buyer.name,
                'date' : order.date,
                'code' : order.code,
                'cart_code' : order.cart.code,
                'bill' : order.bill
            }
            orders_list.append(order_dict)
        return JsonResponse(orders_list,safe=False)
    except Order.DoesNotExist:
        return JsonResponse({'error' : 'order not found'})

def order_item_by_seller(request, seller_name):
    try:
        orders = Order_item.objects.filter(seller__name = seller_name)
        orders_list = []
        for order_item in orders:
            order_item : Order_item
            order_dict = {
                'order_code' : order_item.order.code,
                'buyer' : order_item.order.buyer.name,
                'seller' : order_item.seller.name,
                'product' : order_item.product.name,
                'bill' : order_item.price
            }
            orders_list.append(order_dict)
        return JsonResponse(orders_list,safe=False)
    except Order.DoesNotExist:
        return JsonResponse({'error' : 'order not found'})
    
def order_item_by_product(request, product_name):
    order_items = Order_item.objects.filter(product__name = product_name)
    order_items_list = []
    for order_item in order_items:
        order_item : Order_item
        order_item_dict = {
            'order_code' : order_item.order.code,
            'buyer' : order_item.order.buyer.name,
            'product' : order_item.product.name,
            'bill' : order_item.price
        }
        order_items_list.append(order_item_dict)
    return JsonResponse(order_items_list, safe=False)

def order_by_code(request, code_input):
    try:
        order = Order.objects.get(code = code_input)
        order_dict = {
                'buyer' : order.buyer.name,
                'date' : order.date,
                'code' : order.code,
                'cart_code' : order.cart.code,
                'bill' : order.bill
            }
        return JsonResponse(order_dict, safe=False)
    except Order.DoesNotExist:
        return JsonResponse({'error' : 'that order code does not exist'})



