from django.urls import path
from .views import *

app_name = 'admin'

urlpatterns = [
    path('', LoginClassBaseView.as_view(), name = 'login'),
    path('dashboard/', DashboardClassBaseView.as_view(), name = 'dashboard'),
    path('logout/', LogoutClassBaseView.as_view(), name = 'logout'),
    path('positions/', PositionsClassBaseView.as_view(), name = 'positions'),
    path('employeelist/<path:position>/', GetEmployeeClassBaseView.as_view(), name = 'getemployeelist'),
    path('datelogs/<path:employee_id>/', DateClassBaseView.as_view(), name = 'datelogs'),
    path('timelogs/<path:date>/', TimeClassBaseView.as_view(), name = 'timelogs'),
    path('generatereport/', generatereport, name = 'generatereport'),
]