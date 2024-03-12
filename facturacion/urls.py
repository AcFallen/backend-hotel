from django.urls import path
from .views import *

urlpatterns = [
    path('generar-boleta/', view=generarBoleta),
    path('consultar-boleta/<str:serie>/<int:numero>', view=consultarBoleta),
]
