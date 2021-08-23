from rest_framework import serializers

from apps.vehicle.models import VehicleOrModel, VehicleOrBreakdownPaymentModel

class APISerializerVehicleOrBp(serializers.ModelSerializer):
    class Meta:
        model = VehicleOrBreakdownPaymentModel
        fields = ('__all__')

class APISerializerVehicleOr(serializers.ModelSerializer):
    fk_orbp_rn = APISerializerVehicleOrBp(many = True)

    class Meta:
        model = VehicleOrModel
        fields = ('__all__')