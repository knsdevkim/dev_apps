from django.urls import path

from apps.media.models import MediaModel, DocumentModel
from .views import *

app_name = 'operator'

urlpatterns = [
    # OPERATOR LIST PATH

    path('list/', OperatorListView.as_view(), name = 'operatorList'),

    # OPERATOR DETAILS PATH

    path('<uuid:pk>/', OperatorDetailView.as_view(), name = 'operatorDetail'),

    # OPERATOR SEARCH & FILTER

    path('search/', operator_search, name = 'operatorSearch'),

    # OPERATOR CREATE PATH

    path('create/', new_operator, name = 'operatorCreate'),

    # OPERATOR UPDATE PATH

    path('edit/<uuid:pk>/', update_operator, name = 'operatorUpdate'),

    # OPERATOR DELETE PATH

    path('delete/<uuid:pk>/', OperatorDeleteView.as_view(model = OperatorModel, to_reverse = 'apps:operator:operatorList'), name = 'operatorDelete'),
]