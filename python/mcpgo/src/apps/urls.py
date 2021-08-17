from django.urls import path


from .views import *

app_name = 'apps'


urlpatterns = [
    # BACKEND FUNCTION
    path('approve/account/<int:pk>/', approve_account, name = 'approve'),

    # AUTHENTICATION VIEW
    path('', AuthenticateLoginView.as_view(), name = 'login'),
    path('logout/', AuthenticateLogoutView.as_view(), name = 'logout'),

    # TEMPLATE VIEW
    path('dashboard/', dashboard, name = 'dashboard'),

    # CREATE VIEW
    path('syncfile/', SyncFileFormView.as_view(), name = 'syncfile'),
    path('newaccount/', AccountCreateView.as_view(), name = 'newaccount'),


    # DELETE VIEW
    path('deleteaccount/<int:pk>/', AccountDeleteView.as_view(), name = 'deleteaccount'),

    # LIST VIEW
    path('accountlist/', AccountListView.as_view(), name = 'accountlist'),
    path('gtmlist/', GtmListView.as_view(), name = 'gtmlist'),
    path('saleslist/<path:gtm>/', SalesListView.as_view(), name = 'saleslist'),
    path('customerlist/<path:salesperson>/', CustomerListView.as_view(), name = 'customerlist'),
    path('datalist/', AssignedGtmListView.as_view(), name = 'datalist'),

    # DETAIL VIEW
    path('customerinfo/<int:pk>/', CustomerInfoDetailView.as_view(), name = 'customerinfo'),
]
