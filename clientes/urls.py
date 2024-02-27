from django.urls import path
from .views import *

urlpatterns = [
    path('',view=ClientesController.as_view())
]
