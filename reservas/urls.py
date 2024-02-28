from django.urls import path
from .views import *

urlpatterns = [
    path('',view=ReservasController.as_view())
]
