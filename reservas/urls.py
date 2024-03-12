from django.urls import path
from .views import *

urlpatterns = [
    path('',view=CrearReservaController.as_view()),
    path('lista/',view=ListaDeReservasController.as_view()),
    path('<int:pk>/',view=ObtnerReservaController.as_view()),
    path('<int:id>/actualizar-estado/' ,view=ActualizarEstadoReservaController.as_view()),
    # path('generar-boleta/', view=GenerarBoletaController.as_view()),
    # path('consultar-boleta/<str:serie>/<int:numero>', view=GenerarBoletaController.as_view()),
]
