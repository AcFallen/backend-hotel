from django.db import models

# Create your models here.
class Cliente (models.Model):
    id = models.AutoField(primary_key=True , null=False)
    dni = models.IntegerField(null=False, unique=True)
    nombre = models.TextField(null=False)
    apellido_paterno = models.TextField(null=False)
    apellido_materno = models.TextField(null=False)
    telefono = models.IntegerField(null=False)
    
    class Meta:
        db_table = 'clientes'