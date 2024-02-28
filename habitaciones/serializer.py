from rest_framework import serializers
from .models import *

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        exclude = ['id']

class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'
        
class HabitacionInfoSerializer(serializers.ModelSerializer):
    tipo = TipoSerializer(source='tipoId')
    
    class Meta:
        model = Habitacion
        #fields = '__all__'
        exclude = ['tipoId']
        
class HabitacionDisponibilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model= Habitacion
        fields = ['disponible']