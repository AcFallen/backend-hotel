from rest_framework import serializers
from .models import UsuarioModel

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UsuarioModel
        fields = ['nombre', 'apellido' , 'correo', 'password' , 'tipo_usuario']
        
class MostrarPerfilSerializer(serializers.ModelSerializer):
     class Meta: 
        model = UsuarioModel
        exclude = ['password' , 'is_staff' , 'is_active' , 'groups', 'user_permissions' , 'last_login' , 'is_superuser']

class ActualizarPerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=UsuarioModel
        fields = ['nombre', 'apellido' , 'correo', 'password' ]