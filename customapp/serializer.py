from rest_framework import serializers
from customapp.models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        
        fields = '__all__'  # Serialize all fields of the Flight model