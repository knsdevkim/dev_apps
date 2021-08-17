from django.urls import path, include

from apps.category.views import *

app_name = 'apps'

urlpatterns = [

    # Dashboard URL

    path('', include('apps.dashboard.urls', namespace= 'dashboard')),

    # Category URL
    
    path('category/', include('apps.category.urls', namespace = 'category')),

    # Product URL

    path('product/', include('apps.product.urls', namespace = 'product')),

    # Cashier URL

    path('cashier/', include('apps.cashier.urls', namespace = 'cashier')),
]