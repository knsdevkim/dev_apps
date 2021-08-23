from django.urls import path

from .views import *

app_name = 'api'

urlpatterns = [
    # List

    path('or/', APIGenericVehicleOr.as_view(), name = 'vehicleOrList'),

    # Detail OR

    path('or/<uuid:id>/', APIGenericVehicleOr.as_view(), name = 'vehicleOrDetail'),
]