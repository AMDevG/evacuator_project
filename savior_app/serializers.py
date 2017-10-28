from .models import Evacuator
from rest_framework import serializers


class EvacuatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evacuator
        fields = ('evacuatorID', 'lat', 'lng', 'currentCapacity', 'maxCapacity', 'active' )

