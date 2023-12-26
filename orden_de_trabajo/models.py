from django.db import models
from clientes.models import clientes

from empleados.models import Empleados
from unidades.models import unidades
# Create your models here.


OPCIONES_TIPO_ORDEN =[
        ('No tercerizada','No tercerizada'),
        ('Tercerizada','Tercerizada')
]

class Orden_trabajo(models.Model):
    #Relacion uno a muchos de las tablas Clientes
    Cliente = models.ForeignKey(clientes, on_delete=models.CASCADE)
    #Relacion uno a muchos de las tablas Empleados
    Id_Conductor = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    #------------------
    #Relacion uno a muchos de las tablas Unidades
    Id_Vehiculo = models.ForeignKey(unidades, on_delete=models.CASCADE)
    #------------------
    Origen = models.CharField(max_length=20)
    Destino = models.CharField(max_length=20)
    Detalles = models.CharField(max_length=20)
    Peso = models.DecimalField(max_digits=20, decimal_places=2)
    Fecha_Emision = models.DateField()
    Descripcion = models.CharField(max_length=300)
    Monto_Cotizacion = models.DecimalField(max_digits=20, decimal_places=2)
    Estado = models.BooleanField()
    Tipo_orden_de_trabajo = models.CharField(max_length=20, choices=OPCIONES_TIPO_ORDEN)

    def __str__(self):
        return f"ODT-{self.id}"