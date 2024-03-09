from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status , permissions , generics

from .models import *
from .serializer import *

from drf_yasg.utils import swagger_auto_schema

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.

# class ClientesController(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self,request):
#         resultado = Cliente.objects.all()
        
#         serializador = ClienteSerializer(instance=resultado , many = True)
#         return Response( data={
#             'message': 'Estos son todos los clientes',
#             'content': serializador.data
#         }, status=status.HTTP_200_OK)
    
#     @swagger_auto_schema(request_body=ClienteSerializer)
#     def post(self,request):
#         serializador = ClienteSerializer(data=request.data)
#         if serializador.is_valid():
#             serializador.save()
            
#             return Response(data={
#                 'message': 'Cliente creado con exito'
#             },status=status.HTTP_201_CREATED)
#         else:
#             return Response(data={
#                 'message': 'Error al crear cliente',
#                 'content': serializador.errors
#             },status=status.HTTP_400_BAD_REQUEST)
        
class ClientesListController(generics.ListCreateAPIView):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields  = ('id','nombre','dni')
    search_fields = ('id','nombre','dni')