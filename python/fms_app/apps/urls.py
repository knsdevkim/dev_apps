from django.urls import path, include

from .views import *

app_name = 'apps'

urlpatterns = [
    path('', dashboard, name = 'dashboard'),
    path('vehicle/', include('apps.vehicle.urls', namespace = 'vehicle')),
    path('operator/', include('apps.operator.urls', namespace = 'operator')),
    path('media/', include('apps.media.urls', namespace = 'media')),
    path('document/', include('apps.media.urls', namespace = 'document')),
]