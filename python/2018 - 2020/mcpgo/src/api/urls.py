from django.urls import path

from .views import *

app_name = 'api'

urlpatterns = [
    path('login/', ObtainAuthToken.as_view(), name = 'login'),
    path('getall/', McpmasterlistAPI.as_view(), name = 'getall'),
    path('mcpdata/', McpDataAPI.as_view(), name = 'mcpdata'),
    path('createuser/', RegisterUserAPI.as_view(), name = 'createuser'),
]
