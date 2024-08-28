from django.urls import path
from .views import *
urlpatterns = [
    path('',list_product),
    path('category/<str:category>', category),
    path('buy/<str:name>', buy),
    path('seller/<str:name>', seller),
    path('add_product', add_product),
    path('add_comment', add_comment),
    path('add_rate', add_rate),

]
