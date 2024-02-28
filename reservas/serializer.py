from rest_framework import serializers
from .models import Reserva
from habitaciones.serializer import HabitacionSerializer
from clientes.serializer import ClienteSerializer

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
        
class ReservaInfoSeializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(source='clienteId')
    habitacion = HabitacionSerializer(source='habitacionId')
    
    class Meta:
        model = Reserva
        fields = '__all__'
        