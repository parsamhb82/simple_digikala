from django.http.response import JsonResponse
from .models import Product,Rate,Comment
from django.shortcuts import get_object_or_404


def list_product(request):
    products = Product.objects.all()
    my_product_list = []
    for item in products:
            ticket_dictionary = {
                "name": item.name,
                "price": item.price,
                "category": item.category.name,
                "seller": item.seller.username,
                "stock": item.stock,
            }
            my_product_list.append(ticket_dictionary)
    return JsonResponse(my_product_list, safe=False)

def category(request,category):
    products = Product.objects.filter(category__name=category)
    my_product_list = []
    if products.exists():
        for item in products:
            ticket_dictionary = {
                "name": item.name,
                "price": item.price,
                "category": item.category.name,
                "seller": item.seller.username,
                "stock": item.stock,
                }
            my_product_list.append(ticket_dictionary)
    return JsonResponse(my_product_list, safe=False)




def buy(request, name):
    try:
        products = Product.objects.get( name=name)
        comments = Comment.objects.filter(product=products)
        rate = Rate.objects.filter(product=products).count()


        if rate > 0:
            total_rating = round(products.total_rate() / rate, 2)
        else:
            total_rating = "-"


        ticket_dictionary = {
            "name": products.name,
            "price": products.price,
            "category": products.category.name,
            "seller": products.seller.username,
            "stock": products.stock,
            "description": products.description,
            'total_rating': total_rating,
            'comments': [comment.comment_text for comment in comments],
        }

        return JsonResponse(ticket_dictionary, safe=False)
    except Product.DoesNotExist:
        return JsonResponse({})



def seller(request,name):
    products = Product.objects.filter(seller__username=name)
    my_product_list = []
    if products.exists():
        for item in products:
            ticket_dictionary = {
                "title": item.name,
                "source": item.price,
                "destination": item.description
            }
            my_product_list.append(ticket_dictionary)
    return JsonResponse(my_product_list, safe=False)






