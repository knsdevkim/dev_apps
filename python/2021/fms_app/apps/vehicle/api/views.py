from rest_framework import generics, mixins

from .serializers import *

from apps.vehicle.models import VehicleOrModel, VehicleOrBreakdownPaymentModel

class APIGenericVehicleOr(generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    serializer_class = APISerializerVehicleOr
    queryset         = VehicleOrModel.objects.all()

    lookup_field = 'id'

    def get(self, request, id = None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)