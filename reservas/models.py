from django.db import models
from habitaciones.models import Habitacion
from clientes.models import Cliente
from django.utils import timezone



# Create your models here.
class Reserva(models.Model):
    id = models.AutoField(primary_key=True , null=False)
    clienteId = models.ForeignKey(to=Cliente,
                                on_delete=models.PROTECT)
    habitacionId = models.ForeignKey(to=Habitacion,
                                   on_delete=models.PROTECT)
    ESTADO_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('pagada', 'Pagada'),
        ('cancelada', 'Cancelada'),
        ('finalizada', 'Finalizada'),
    )
    
    estado = models.CharField(choices=ESTADO_CHOICES , default='pendiente')
    metodo_de_pago = models.CharField(null=False)
    hora_ingreso = models.DateTimeField(default=timezone.now)
    hora_salida = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        db_table = 'reservas'