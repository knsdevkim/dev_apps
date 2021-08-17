from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    # ==================== CREDENTIALS REQUIRED =======================
    path('', LoginViewUser.as_view(), name = 'login'),
    path('logout/', LogoutViewUser.as_view(), name = 'logout'),

    # ====================     STATIC VIEWS     =======================
    path('panel/', panel, name = 'panel'),

    # ====================     LIST VIEWS       =======================
    path('users/', ListViewUsers.as_view(), name = 'users'),

    # ====================     CREATE VIEWS     =======================
    path('createadmin/', CreateViewUser.as_view(), name = 'createadmin'),
    path('sync/', FormViewSync.as_view(), name = 'sync'),

    # ====================     UPDATE VIEWS     =======================
    path('updateuser/<int:pk>/', UpdateViewUser.as_view(), name = 'updateuser'),

    # ====================     DELETE VIEWS     =======================
    path('delete/<int:pk>/', DeleteViewUser.as_view(), name = 'deleteuser'),
]
