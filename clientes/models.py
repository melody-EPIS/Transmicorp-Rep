from django.db import models
from django.core.validators import RegexValidator
from django.forms import ValidationError


CLIENTE_VALORACION = [
	('Malo', 'Malo'),
	('Bueno', 'Bueno'),
	('Excelente', 'Excelente')
]

class clientes(models.Model):
	Ruc_Clientes = models.CharField(max_length=11, unique=True)
	Cliente_telefono = models.CharField(max_length=9)
	Cliente_email = models.EmailField()
	Cliente_direccion = models.CharField(max_length=100)
	Valoracion = models.CharField(max_length=20, default='Valor Predeterminado', choices=CLIENTE_VALORACION)
	Tipo_Mercaderia = models.CharField(max_length=200)

	def __str__(self):
		return f"RUC - {self.Ruc_Clientes}"
	
class clienteRUC10(clientes):
	Cliente_Nombre = models.CharField(max_length=100)
	Cliente_Apellido = models.CharField(max_length=100)

class clienteRUC20(clientes):
	Nombre_Empresa = models.CharField(max_length=100)     
        
        

        
      
