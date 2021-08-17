from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from apps.models import *


# Create your views here.
def test(request):
    return HttpResponse('N1S SERVER CONNECTED . . . BUFFERING DATA . . . ')


class ObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(ObtainAuthToken, self).post(request, *args, **kwargs)
        token    = Token.objects.get(key = response.data['token'])
        user     = Users.objects.get(pk = token.user_id)
        return Response({
            'token': token.key,
            'id': token.user_id,
            'user_type': user.user_type,
            'account_status': user.account_status,
            'fullname': user.link_mcp,
            'userfullname': f'{user.first_name.upper()}, {user.last_name.upper()}'
        })

class RegisterUserAPI(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = UserAPISerializer
    queryset         = Users.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request)


class McpmasterlistAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = McpAPISerializer
    queryset         = Mcpmasterlist.objects.all()

    authentication_classes = [TokenAuthentication]
    permission_classes     = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request)

class McpDataAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = McpAPISerializer
    queryset         = Mcpmasterlist.objects.all()

    authentication_classes = [BasicAuthentication]
    permission_classes     = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request)
