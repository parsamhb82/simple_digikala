from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('product_app.urls')),
    path('order/', include('order_app.urls')),
    path('cart/', include('cart_app.urls'))

]
