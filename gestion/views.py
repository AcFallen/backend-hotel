from rest_framework import generics , response , status , request ,permissions
from .serializer import *
from .permissions import Administrador

from drf_yasg.utils import swagger_auto_schema


# Create your views here.


class RegistroUsuarioController(generics.CreateAPIView):
    permission_classes=[permissions.IsAuthenticated , Administrador]
    @swagger_auto_schema(request_body=RegistroUsuarioSerializer)
    def post(self, request: request.Request):
        serializador = RegistroUsuarioSerializer(data=request.data)
        
        if serializador.is_valid():
            nuevo_usuario = UsuarioModel(**serializador.validated_data)
            nuevo_usuario.set_password(serializador.validated_data.get('password'))
            
            nuevo_usuario.save()
            
            return response.Response(data={
                'message':'Usuario creado exitosamente',             
            },status=status.HTTP_201_CREATED)
        else:
            return response.Response(data={
                'message':'Error al registrar el usuario',
                'content': serializador.errors
            },status=status.HTTP_400_BAD_REQUEST)
            
# class PerfilUsuarioController(generics.RetrieveAPIView):
    
#     permission_classes = [permissions.IsAuthenticated]
#     def get(self , request : request.Request):
        
#         usuario_encontrado = MostrarPerfilSerializer(instance= request.user)
        
#         return response.Response (data={
#             'content': usuario_encontrado.data
#         })
    
class PerfilUsuarioController(generics.RetrieveAPIView):
    serializer_class = MostrarPerfilSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        usuario_encontrado = self.serializer_class(instance=request.user)
        return response.Response(data={
            'content': usuario_encontrado.data
        })
    
class ActualizarPerfilController(generics.UpdateAPIView):
    permission_classes=[ permissions.IsAuthenticated , Administrador ]
    queryset = UsuarioModel.objects.all()
    serializer_class = ActualizarPerfilUsuarioSerializer