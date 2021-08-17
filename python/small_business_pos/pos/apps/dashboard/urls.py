from django.urls import path

from .views import *

app_name = 'dashboard'

urlpatterns = [
    # Index

    path('', dashboard, name = 'dashboard'),
]