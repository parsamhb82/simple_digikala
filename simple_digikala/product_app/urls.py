from django.urls import path
from . import views
urlpatterns = [
    path('',views.list_product),
    path('category/<str:category>', views.category),
    path('buy/<str:name>', views.buy),
    path('seller/<str:name>', views.seller),

]
