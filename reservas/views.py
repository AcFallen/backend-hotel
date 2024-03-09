from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status , permissions , generics

from .models import *
from .serializer import *

from drf_yasg.utils import swagger_auto_schema

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

# class ReservasController(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self,request):
#         resultado = Reserva.objects.all()
        
#         serializador = ReservaInfoSeializer(instance=resultado , many=True)
#         return Response(data={
#             'message': 'Lista de reservas',
#             'content': serializador.data
#         })

#     @swagger_auto_schema(request_body=ReservaSerializer)
#     def post(self,request):
#         serializador = ReservaSerializer(data=request.data)
        
#         if serializador.is_valid():
#             serializador.save()
            
#             return Response(data={
#                 'message': 'Reserva creada con exito'
#             }, status=status.HTTP_201_CREATED)
#         else:
#             return Response(data={
#                 'message':'Error al crear una reserva',
#                 'content': serializador.errors
#             }, status=status.HTTP_400_BAD_REQUEST)
        

class CrearReservaController(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ListaDeReservasController(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Reserva.objects.all()
    serializer_class = ReservaInfoSeializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields  = ('id','estado')
    search_fields = ('id','estado')

class ObtnerReservaController(generics.RetrieveAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaInfoSeializer
    filter_backends = (DjangoFilterBackend, SearchFilter)

class ActualizarEstadoReservaController(generics.UpdateAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ActulizarEstadoSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    lookup_field = 'id'

    def patch(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

