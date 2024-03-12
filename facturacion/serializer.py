from rest_framework import serializers

class GenerarBoletaSerializer(serializers.Serializer):
    documento_usuario=serializers.CharField(max_length = 8 , min_length=8 , allow_null = False , required =True)
    nombre_usuario = serializers.CharField(required =True)
    cantidad_dias = serializers.IntegerField( min_value = 0 , required = True) 
    habitacion_id = serializers.IntegerField( min_value = 0 , required = True)
    numero_factura = serializers.IntegerField(min_value = True , required = True)