from django.db import models
from django.core.validators import RegexValidator

ESTADO_UNIDAD = [
    ('Disponible', 'Disponible'),
    ('En Mantenimiento', 'En Mantenimiento'),
    ('En Tránsito', 'En Tránsito')
]

TIPO_UNIDAD =[
    ('Camión articulado', 'Camión articulado'),
    ('Camión rígido', 'Camión rígido'),
    ('Camión cerrado', 'Camión cerrado'),
    ('Camión contenedor', 'Camión contenedor')
]



class unidades(models.Model):
    Placa_Vehiculo = models.CharField(max_length=100)
    Tipo_de_Vehiculo = models.CharField(max_length=100, choices=TIPO_UNIDAD)
    Capacidad_Carga = models.IntegerField()
    Estado_unidad = models.CharField(max_length=30, choices=ESTADO_UNIDAD)
    Observaciones = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Placa_Vehiculo}"
