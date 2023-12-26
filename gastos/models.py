from django.db import models
from orden_de_trabajo.models import Orden_trabajo
from facturas.models import factura
from inventario.models import inventario
# Create your models here.
TIPO_GASTO = [
    ('1','Gasto Fijo'),
    ('2','Gasto variable'),
]
AREA_GASTO = [
    ('1','Gasto Administrativo'),
    ('2','Gasto en Combustible'),
    ('3','Gasto en Mantenimiento'),
    ('4','Gasto en Repuestos'),
    ('5','Gasto en Salarios/Sueldos'),
    ('6','Gasto en Estibaje'),
    ('7','Gastos en impuestos tributarios'),
]
class gastos(models.Model):
    #Relacion uno a muchos de las tablas Factura, orden de trabajdo y Inventario
    # con la tabla gastos.
    Factura = models.ForeignKey(factura, on_delete=models.CASCADE)
    Orden_de_trabajo = models.ForeignKey(Orden_trabajo, on_delete=models.CASCADE)
    Inventario = models.ForeignKey(inventario, on_delete=models.CASCADE)
    # -------------
    Codigo_de_boleta = models.IntegerField()
    Tipo_de_gasto = models.CharField(max_length=100, default='Valor Predeterminado', choices=TIPO_GASTO)
    Area_de_gasto = models.CharField(max_length=100, default='Valor Predeterminado', choices=AREA_GASTO)
    Descripcion = models.TextField(max_length=500)
    Monto_gastado = models.DecimalField(
        max_digits=7,  
        decimal_places=2, 
    )
    Fecha_boleta = models.DateField()   
    Documento_boleta = models.FileField(upload_to='DocGastos/')

    def __str__(self):
        return f"Gasto {self.id}"