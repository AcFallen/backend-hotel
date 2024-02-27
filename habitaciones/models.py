from django.db import models

# Create your models here.

class Tipo (models.Model):
    id =  models.AutoField(primary_key=True , null=False)
    nombre = models.TextField(null=False)
    
    class Meta:
        db_table = 'tipo'
        
class Habitacion(models.Model):
    id = models.AutoField(primary_key=True , null=False)
    numero = models.IntegerField(null=False)
    tipoId = models.ForeignKey(to=Tipo,
                               db_column='tipo_id',
                               on_delete=models.PROTECT)
    capacidad = models.IntegerField(null=False)
    precio = models.IntegerField(null=False)
    descripcion = models.TextField(null=False)
    imagen = models.ImageField(null=True, blank=True)
    disponible = models.BooleanField(null=False)

    
    class Meta:
        db_table = 'habitaciones'
