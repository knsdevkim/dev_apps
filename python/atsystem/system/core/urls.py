from django.urls import path

from .views import *

app_name = 'core'

urlpatterns = [
    path('', DashboardClassBaseView.as_view(), name='dashboard'),
    path('upload/', UploadClassBaseView.as_view(), name='upload'),
    path('update/folder/<int:pk>/', FolderUpdateClassBaseView.as_view(), name='updatefolder'),
    path('update/ada/<int:pk>/', AdaUpdateClassBaseView.as_view(), name='updateada'),
    path('update/it/<int:pk>/', ItEquipmentUpdateClassBaseView.as_view(), name='updateit'),
    path('view/folder/<path:type>/', FolderClassBaseView.as_view(), name='folder'),
    path('view/record/<path:type>/<int:folder>/', RecordClassBaseView.as_view(), name='record'),
    path('print/it/<int:pk>/', itprint, name='itprint'),
    path('print/ada/<int:pk>/', adaprint, name='adaprint'),
    path('print/get/it/<int:pk>/', getitprint, name='getitprint'),
    path('print/get/ada/<int:pk>/', getadaprint, name='getadaprint'),
    path('deletefolder/<path:type>/<int:pk>/', FolderDeleteClassBaseView.as_view(), name='deletefolder'),
    path('generatexls/<int:folder>/', generate_excel, name='generate_excel'),
    path('claim/', claim, name='claim'),
]