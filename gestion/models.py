from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from .auth_manager import UsuarioManager

# Create your models here.

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField(unique =True , null=False)
    password = models.TextField(null=False)
    tipo_usuario = models.CharField(max_length=100 , choices = [('ADMINISTRADOR' , 'ADMINISTRADOR'),
                                                                ('RECEPCIONISTA','RECEPCIONISTA')] , default='ADMINISTRADOR')
    
    is_staff = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'correo'
    
    REQUIRED_FIELDS = ['nombre' , 'apellido']
    
    objects = UsuarioManager()
    
    class Meta:
        db_table = 'usuarios'
    