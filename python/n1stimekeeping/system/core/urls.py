from django.urls import path
from .views import (
    SyncFileClassBaseView,
    TimeKeepingClassBaseView
)

app_name = 'core'

urlpatterns = [
    path('sync/', SyncFileClassBaseView.as_view(), name='syncfile'),
    path('', TimeKeepingClassBaseView.as_view(), name='timekeeping'),
]
