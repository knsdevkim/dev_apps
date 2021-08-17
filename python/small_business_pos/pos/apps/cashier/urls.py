from django.urls import path

from .views import *

app_name = 'cashier'

urlpatterns = [
    # Index

    path('', cashier, name = 'cashier'),
]