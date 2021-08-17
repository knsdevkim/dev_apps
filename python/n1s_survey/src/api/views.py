from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from core.models import *
from api.serializers import *


# Create your views here.

class CreateEvaluationGenericAPIView(GenericAPIView, CreateModelMixin):
    serializer_class = EvaluationSerializer
    queryset         = Evaluation.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request)


class CreateTrainingMemoGenericAPIView(GenericAPIView, CreateModelMixin):

    serializer_class = TraningMemoSerializer
    queryset         = TrainingMemo.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request)
