from rest_framework import serializers
from .models import Reserva
from habitaciones.serializer import HabitacionSerializer
from clientes.serializer import ClienteSerializer
from habitaciones.serializer import HabitacionSerializer

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

class ActulizarEstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields =  ['estado']


#-------------------------------------------------------------------#


class GenerarBoletaSerializer(serializers.ModelSerializer):
    documento_usuario=serializers.CharField(max_length = 8 , min_length=8 , allow_null = False , required =True)
    nombre_usuario = serializers.CharField(required =True)
    cantidad_dias = serializers.IntegerField( min_value = 0) 
    habitacion_id = serializers.IntegerField( min_value = 0)

    class Meta :
        model = Reserva
        #fields = '__all__'
        exclude = ['metodo_de_pago' , 'clienteId' , 'habitacionId']

