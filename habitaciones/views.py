from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view


from .models import *
from .serializer import *

from drf_yasg.utils import swagger_auto_schema
# Create your views here.

class TiposController(APIView):
    def get(self,request):
        resultado = Tipo.objects.all()
        
        serializador = TipoSerializer(instance=resultado , many=True)
        return Response(data={
            'message': 'Estos son todos los tipos de habitaciones',
            'content': serializador.data
        })

    @swagger_auto_schema(request_body=TipoSerializer)    
    def post(self,request):
        serializador = TipoSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            
            return Response(data={
                'message': 'Tipo de habitacion creada'
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al crear el tipo de habitacion',
                'content': serializador.errors
            },status=status.HTTP_400_BAD_REQUEST)
            
class TipoController(APIView):
    
    def get(self , request, id):
        tipo_encontrado = Tipo.objects.filter(id=id).first()
        if not tipo_encontrado:
            return Response(data={
                'message': 'El tipo de habitacion no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializador = TipoSerializer(instance=tipo_encontrado)
        return Response(data={
            'content': serializador.data
        }, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=TipoSerializer)    
    def put(self,request,id):
        tipo_encontrado = Tipo.objects.filter(id=id).first()
        if not tipo_encontrado:
            return Response(data={
                'message': 'El tipo de habitacion no existe'
            }, status=status.HTTP_404_NOT_FOUND)
            
        serializador = TipoSerializer(data=request.data)
        
        if serializador.is_valid():
            serializador.update(instance=tipo_encontrado ,
                                validated_data=serializador.validated_data)
            return Response(data={
                'message': 'Tipo de habitacion actualizada'
            }, status=status.HTTP_200_OK)
        else:
            return Response(data={
                'message': 'Error al actualizar el tipo de habitacion',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
    @swagger_auto_schema(request_body=TipoSerializer)
    def delete(self , request, id):
        tipo_encontrado = Tipo.objects.filter(id=id).first()
        if not tipo_encontrado:
            return Response(data={
                'message': 'El tipo de habitacion no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        Tipo.objects.filter(id=id).delete()
        
        return Response(data=None,status=status.HTTP_204_NO_CONTENT)

class HabitacionesController(APIView):
    def get(self,request):
        resultado = Habitacion.objects.all()
        
        serializador = HabitacionInfoSerializer(instance=resultado , many=True)
        return Response(data={
            'message': 'Estos son todas las habitaciones',
            'content': serializador.data
        })
    
    def post(self,request):
        serializador = HabitacionSerializer(data=request.data)
        if serializador.is_valid():
            serializador.save()
            
            return Response(data={
                'message': 'Habitacion creada con exito'
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Error al crear habitacion',
                'content': serializador.errors
            },status=status.HTTP_400_BAD_REQUEST)
            
class HabitacionController(APIView):
    def get(self, request, id):
        habitacion_encontrada = Habitacion.objects.filter(id=id).first()
        if not habitacion_encontrada:
            return Response(data={
                'message':'La habitacion no existe'
            }, status=status.HTTP_404_NOT_FOUND)
        serializador = HabitacionInfoSerializer(instance=habitacion_encontrada)
        return Response(data={
            'content': serializador.data
        }, status=status.HTTP_200_OK)    
        
    def put(self,request,id):
        habitacion_encontrada = Habitacion.objects.filter(id=id).first()
        if not habitacion_encontrada:
            return Response(data={
                'message':'La habitacion no existe'
            }, status=status.HTTP_404_NOT_FOUND)
            
        serializador = HabitacionSerializer(data=request.data)
        
        if serializador.is_valid():
            serializador.update(instance=habitacion_encontrada ,
                                validated_data=serializador.validated_data)
            return Response(data={
                'message': 'Habitacion actualizada exitosamente'
            }, status=status.HTTP_200_OK)
        else:
            return Response(data={
                'message': 'Error al actualizar la habitacion',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        habitacion_encontrada = Habitacion.objects.filter(id=id).first()
        if not habitacion_encontrada:
            return Response(data={
                'message':'La habitacion no existe'
            }, status=status.HTTP_404_NOT_FOUND)
            
        Habitacion.objects.filter(id=id).delete()
        
        return Response(data=None, status=status.HTTP_204_NO_CONTENT)
    
@api_view(http_method_names=['PUT'])
def cambiarDisponibilidadHabitacion(request , id):
    
    habitacion_encontrada = Habitacion.objects.filter(id=id).first()
    if not habitacion_encontrada:
        return Response(data={
                'message':'La habitacion no existe'
        }, status=status.HTTP_404_NOT_FOUND)
        
    serializador = HabitacionDisponibilidadSerializer(data=request.data)
    
    if serializador.is_valid():
        serializador.update(instance=habitacion_encontrada,
                            validated_data=serializador.validated_data)
        
        return Response(data={
            'message': 'Disponibilidad Actualizada',
            'content': serializador.data
        },status=status.HTTP_200_OK)
    else:
         return Response(data={
            'message': 'Error al actualizar habitacion',
            'content': serializador.errors
        }, status=status.HTTP_400_BAD_REQUEST)