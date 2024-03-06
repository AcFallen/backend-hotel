from rest_framework.permissions import BasePermission

class Administrador(BasePermission):
    message = 'Solo los administradores pueden acceder a estas rutas'
    def has_permission(self, request, view):
        tipoUsuario = request.user.tipo_usuario
        
        if tipoUsuario == 'ADMINISTRADOR':
            return True
        
        else:
            return False
        
class Recepcion(BasePermission):
    message = 'Solo los recepcionistas pueden acceder a estas rutas'
    def has_permission(self, request, view):
        tipoUsuario = request.user.tipo_usuario
        
        if tipoUsuario == 'RECEPCIONISTA':
            return True
        
        else:
            return False