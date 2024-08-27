from django.http.response import JsonResponse
from cart_app.models import Cart, Cart_item

def cart_list_func(request):
    carts = Cart.objects.all()
    carts_list = []
    for cart in carts:
        cart : Cart
        cart_dict = {
            'buyer' : cart.buyer.name,
            'code' : cart.code,
            'bill' : cart.bill,
            'is_finalized' : cart.is_finalized
        }
        carts_list.append(cart_dict)
    return JsonResponse(carts_list,safe=False)

def cart_item_func(request):
    cart_items = Cart_item.objects.all()
    cart_items_list = []
    for cart_item in cart_items:
        cart_item : Cart_item
        cart_item_dict = {
            'cart_code' : cart_item.cart.code,
            'buyer' : cart_item.cart.buyer.name,
            'seller' : cart_item.seller.name,
            'product' : cart_item.product.name,
            'bill' : cart_item.price
        }
        cart_items_list.append(cart_item_dict)
    return JsonResponse(cart_items_list, safe=False)

def cart_by_buyer(request, buyer_name):
    try:
        carts = Cart.objects.filter(buyer__name = buyer_name)
        carts_list = []
        for cart in carts:
            cart : Cart
            cart_dict = {
                'buyer' : cart.buyer.name,
                'code' : cart.code,
                'bill' : cart.bill,
                'is_finalized' : cart.is_finalized
            }
            carts_list.append(cart_dict)
        return JsonResponse(carts_list,safe=False)
    except cart.DoesNotExist:
        return JsonResponse({'error' : 'cart not found'})

def cart_item_by_seller(request, seller_name):
    try:
        cart_items = Cart_item.objects.filter(seller__name = seller_name)
        carts_list = []
        for cart_item in cart_items:
            cart_item : Cart_item
            cart_dict = {
                'cart_code' : cart_item.cart.code,
                'buyer' : cart_item.cart.buyer.name,
                'seller' : cart_item.seller.name,
                'product' : cart_item.product.name,
                'bill' : cart_item.price
            }
            carts_list.append(cart_dict)
        return JsonResponse(carts_list,safe=False)
    except Cart.DoesNotExist:
        return JsonResponse({'error' : 'cart not found'})
    
def cart_item_by_product(request, product_name):
    cart_items = Cart_item.objects.filter(product__name = product_name)
    cart_items_list = []
    for cart_item in cart_items:
        cart_item : Cart_item
        cart_item_dict = {
            'cart_code' : cart_item.cart.code,
            'buyer' : cart_item.cart.buyer.name,
            'seller' : cart_item.seller.name,
            'product' : cart_item.product.name,
            'bill' : cart_item.price
        }
        cart_items_list.append(cart_item_dict)
    return JsonResponse(cart_items_list, safe=False)

def cart_by_code(request, code_input):
    try:
        cart = Cart.objects.get(code = code_input)
        cart_dict = {
                'buyer' : cart.buyer.name,
                'code' : cart.code,
                'bill' : cart.bill,
                'is_finalized' : cart.is_finalized
            }
        return JsonResponse(cart_dict, safe=False)
    except Cart.DoesNotExist:
        return JsonResponse({'error' : 'that cart code does not exist'})


