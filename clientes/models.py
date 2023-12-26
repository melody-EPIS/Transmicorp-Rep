from django.db import models
from django.core.validators import RegexValidator
from django.forms import ValidationError

OPCIONES_TIPO_RUC = [
    ('RUC10', 'RUC10'),
    ('RUC20', 'RUC20')
]

CLIENTE_VALORACION = [
    ('Malo', 'Malo'),
    ('Bueno', 'Bueno'),
    ('Excelente','Excelente')
]

class clientes(models.Model):
    Tipo_Ruc = models.CharField(max_length=5,choices=OPCIONES_TIPO_RUC)
    Ruc_Clientes = models.CharField(max_length=11, unique=True)
    Cliente_Nombre = models.CharField(max_length=100)
    Cliente_Apellido = models.CharField(max_length=100)
    Cliente_telefono = models.CharField(max_length=9)
    Cliente_email = models.EmailField()
    Cliente_direccion = models.CharField(max_length=100)
    Valoracion = models.CharField(max_length=20,default='Valor Predeterminado',choices=CLIENTE_VALORACION)
    Tipo_Mercaderia = models.CharField(max_length=200)

    def __str__(self):
        return f"RUC - {self.Ruc_Clientes}"
