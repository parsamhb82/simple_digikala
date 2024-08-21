from django.http.response import JsonResponse
from accounts.models import Costumer, Seller

def costumers_list_func(request):
    costumers = Costumer.objects.all()
    costumers_list = []
    for costumer in costumers:
        costumer_dict = {
            'name' : costumer.name,
            'city' : costumer.city,
            'username' : costumer.username
        }
        costumers_list.append(costumer_dict)
    
    return JsonResponse(costumers_list, safe=False)

def sellers_list_func(request):
    sellers = Seller.objects.all()
    sellers_list = []
    for seller in sellers:
        seller_dict = {
            'name' : seller.name,
            'city' : seller.city,
            'username' : seller.username
        }
        sellers_list.append(seller_dict)
    
    return JsonResponse(sellers_list, safe=False)

def find_costumers_by_name(request, input_name):
    costumers = Costumer.objects.filter(name = input_name)
    costumers_list = []
    for costumer in costumers:
        costumer_dict = {
            'name' : costumer.name,
            'city' : costumer.city,
            'username' : costumer.username
        }
        costumers_list.append(costumer_dict)
    
    return JsonResponse(costumers_list, safe=False)

def find_sellers_by_name(request, input_name):
    sellers = Seller.objects.filter(name = input_name)
    sellers_list = []
    for seller in sellers:
        seller_dict = {
            'name' : seller.name,
            'city' : seller.city,
            'username' : seller.username
        }
        sellers_list.append(seller_dict)
    
    return JsonResponse(sellers_list, safe=False)

def find_costumers_by_username(request, input_username):
    try:
        costumer = Costumer.objects.get(username=input_username)
        costumer_dict = {
            'name': costumer.name,
            'city': costumer.city,
            'username': costumer.username
        }
        return JsonResponse(costumer_dict, safe=False)
    except Costumer.DoesNotExist:
        return JsonResponse({'error': 'Costumer not found'}, status=404)

def find_sellers_by_username(request, input_username):
    try:
        seller = Seller.objects.get(username=input_username)
        seller_dict = {
            'name' : seller.name,
            'city' : seller.city,
            'username' : seller.username
        }
        return JsonResponse(seller_dict, safe=False)
    except Seller.DoesNotExist:
        return JsonResponse({'error' : 'seller not found'}, status=404)




    
