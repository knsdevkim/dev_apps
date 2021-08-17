from django.urls import path
from .views import *

urlpatterns = [
    path('', WebsiteView.as_view(), name='site'),
    path('article/<path:pathfind>/<int:pk>/', SingleView.as_view(), name='read'),
    path('contactus/', ContactView.as_view(), name='contactus'),
    path('careers/', CareersView.as_view(), name='careers'),
    path('products/', ProductsView.as_view(), name='products'),
]

app_name = 'website'
