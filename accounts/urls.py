from django.urls import path
from accounts.views import costumers_list_func, sellers_list_func,find_costumers_by_name, find_sellers_by_name,find_costumers_by_username,find_sellers_by_username

urlpatterns = [
    path('costumers', costumers_list_func),
    path('sellers', sellers_list_func),
    path('costumers/<str:input_name>', find_costumers_by_name),
    path('sellers/<str:input_name>', find_sellers_by_name),
    path('costumers/find_costumers_by_username/<str:input_username>', find_costumers_by_username),
    path('sellers/find_sellers_by_username/<str:input_username>', find_sellers_by_username)
]