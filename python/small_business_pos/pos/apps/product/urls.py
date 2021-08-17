from django.urls import path

from .views import *

app_name = 'product'

urlpatterns = [

    # Create Path

   path('create/', new_product, name = 'productCreate'),
   
    # List Path

    path('<slug:category>/', ProductListView.as_view(), name = 'productList'),

   # Delete Path

   path('delete/<int:pk>/<path:category>/', ProductDeleteView.as_view(), name = 'productDelete'),
]