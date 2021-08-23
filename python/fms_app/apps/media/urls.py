from django.urls import path

from .views import *

app_name = 'media'

urlpatterns = [
    # MEDIA DOWNLOAD 

    path('download/<path:file>', download, name = 'download'),

    # MEDIA CREATE

    path('upload/<str:type>/<uuid:pk>/', new_media_upload, name = 'uploadMedia'),

    # MEDIA UPDATE

    path('update/', media_upload, name = 'updateMedia'),

    # DOCUMENT CREATE

    path('upload/', document_upload, name = 'uploadDocument'),

    # MEDIA DELETE

    path('vehicle/image/delete_permanently/<uuid:return_pk>/<uuid:pk>/', MediaDeleteView.as_view(model = MediaModel, to_reverse = 'apps:vehicle:vehicleDetails', with_pk = True), name = 'vehicleImageDelete'),
    path('vehicle/document/delete_permanently/<uuid:return_pk>/<uuid:pk>/', MediaDeleteView.as_view(model = DocumentModel, to_reverse = 'apps:vehicle:vehicleDetails', with_pk = True), name = 'vehicleDocumentDelete'),
    path('driver/delete/image/<uuid:return_pk>/<uuid:pk>/', MediaDeleteView.as_view(model = MediaModel, to_reverse = 'apps:operator:operatorDetail', with_pk = True), name = 'operatorImageDelete'),
    path('driver/delete/document/<uuid:return_pk>/<uuid:pk>/', MediaDeleteView.as_view(model = DocumentModel, to_reverse = 'apps:operator:operatorDetail', with_pk = True), name = 'operatorDocumentDelete'),
]