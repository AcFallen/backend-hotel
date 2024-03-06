from django.urls import path
from .views import *

from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('registro' , RegistroUsuarioController.as_view()),
    path('login' , TokenObtainPairView.as_view()),
    path('perfil',PerfilUsuarioController.as_view())
]
