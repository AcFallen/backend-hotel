from django.urls import path
from .views import *

urlpatterns = [
    path('tipos/',view=TiposController.as_view()),
    path('tipo/<int:id>',view=TipoController.as_view()),
    path('',view=HabitacionesController.as_view()),
    path('<int:id>',view=HabitacionController.as_view()),
    path('<int:id>/disponibilidad/',view=cambiarDisponibilidadHabitacion),
    path('disponibles/',view=habitacionesDisponibles),
    path('disponibles/p/',view=habitacionPorTipoDisponibles),
]
