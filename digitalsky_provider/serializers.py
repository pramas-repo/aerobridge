from rest_framework import serializers
from .models import DigitalSkyLog, AircraftRegister



class DigitalSkyLogSerializer(serializers.ModelSerializer):
    ''' A serializer to the drone create view '''

    class Meta:
        model = DigitalSkyLog		
        ordering = ['-created_at']
        exclude = ('created_at',)

class AircraftRegisterSerializer(serializers.ModelSerializer):


    class Meta:
        model = AircraftRegister	
        ordering = ['-created_at']
