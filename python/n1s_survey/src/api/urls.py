from django.urls import path

from api.views import *

app_name = 'api'

urlpatterns = [
    path('survey/', CreateEvaluationGenericAPIView.as_view(), name = 'createsurvey'),
    path('trainingmemo/', CreateTrainingMemoGenericAPIView.as_view(), name = 'createtrainingmemo'),
]
