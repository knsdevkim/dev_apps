from django.urls import path

from core.views import *


app_name = 'core'


urlpatterns = [
    path('', Login.as_view(), name = 'login'),
    path('logout/', Logout.as_view(), name = 'logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('evaluation-list/', EvaluationList.as_view(), name = 'evaluation_list'),
    path('evaluation-details/<int:pk>/', EvaluatedDetails.as_view(), name = 'evaluation_details'),
    path('trainingmemo-list/', TrainingmemoList.as_view(), name = 'trainingmemo_list'),
    path('trainingmemo-details/<int:pk>/', TrainingmemoDetails.as_view(), name = 'trainingmemo_details'),
]
