from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status , permissions

from .models import *
from .serializer import *

from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class ReservasController(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        resultado = Reserva.objects.all()
        
        serializador = ReservaInfoSeializer(instance=resultado , many=True)
        return Response(data={
            'message': 'Lista de reservas',
            'content': serializador.data
        })

    @swagger_auto_schema(request_body=ReservaSerializer)
    def post(self,request):
        serializador = ReservaSerializer(data=request.data)
        
        if serializador.is_valid():
            serializador.save()
            
            return Response(data={
                'message': 'Reserva creada con exito'
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message':'Error al crear una reserva',
                'content': serializador.errors
            }, status=status.HTTP_400_BAD_REQUEST)