from django.urls import path, include

from apps.media.models import MediaModel, DocumentModel
from .views import *

app_name = 'vehicle'

urlpatterns = [
    # VEHICLE LIST PATH

    path('list/', VehicleListView.as_view(), name = 'vehicleList'),

    # VEHICLE DETAILS PATH

    path('<uuid:pk>/', VehicleDetailView.as_view(), name = 'vehicleDetails'),

    # VEHICLE PRINT PATH

    path('print/<str:print_for>/<uuid:pk>/', VehiclePrintView.as_view(), name = 'vehiclePrint'),

    # VEHICLE SEARCH & FILTER PATH

    path('search/', vehicle_search, name = 'vehicleSearch'),

    # VEHICLE CREATE PATH
    
    path('new/<str:new_for>/', VehicleCreateView.as_view(), name = 'vehicleCreate'),
    path('new/<str:new_for>/<uuid:fk>/', VehicleCreateView.as_view(), name = 'vehicleCrCreate'),
    path('new/or', create_vehicle_or, name = 'vehicleOrCreate'),

    # VEHICLE UPDATE PATH

    path('details/edit/<uuid:pk>/', VehicleUpdateView.as_view(model = VehicleModel, form_class = VehicleForm, to_modify = 'details'), name = 'vehicleDetailsUpdate'),
    path('cr/edit/<uuid:fk>/<uuid:pk>/', VehicleUpdateView.as_view(model = VehicleCrModel, form_class = VehicleCrForm, to_modify = 'cr'), name = 'vehicleCrUpdate'),
    path('or/details/create_update/<uuid:pk>/', create_update_vehicle_or, name = 'vehicleOrDetailsCreateUpdate'),
    path('update/status/', update_vehicle_status, name = 'vehicleUpdateStatus'),

    # VEHICLE DELETE PATH

    path('data/delete_permanently/<uuid:pk>/', VehicleDeleteView.as_view(model = VehicleModel, to_reverse = 'apps:vehicle:vehicleList'), name = 'vehicleDelete'),
    path('orbp/delete_permanently/<uuid:return_pk>/<uuid:pk>/', VehicleDeleteView.as_view(model = VehicleOrBreakdownPaymentModel, to_reverse = 'apps:vehicle:vehicleOrDetailsCreateUpdate', with_pk = True), name = 'vehicleOrBpDelete'),

    # API

    path('api/', include('apps.vehicle.api.urls', namespace = 'api')),
]