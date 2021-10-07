from django.urls import path

from .views import ProductListView, new_product

app_name = 'product'

urlpatterns = [
    # List

    path('<uuid:category>/', ProductListView.as_view(), name = 'productlist'),

    # Create

    path('create/', new_product, name = 'productcreate'),
]
