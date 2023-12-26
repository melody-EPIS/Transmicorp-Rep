from django.db import models
from orden_de_trabajo.models import Orden_trabajo
from clientes.models import clientes

class factura(models.Model):
    #Relacion uno a uno con tabla orden de trabajo
    Orden_de_trabajo = models.OneToOneField(Orden_trabajo, on_delete=models.CASCADE)
    #--------------------------
    Fecha_Emision = models.DateField(verbose_name="Fecha de ingreso")
    Id_cliente = models.ForeignKey(
        clientes,
        on_delete=models.CASCADE,
        to_field="Ruc_Clientes",
        verbose_name="Nombre del cliente")
    Importe = models.FloatField()
    IGV = models.FloatField()
    Detraccion = models.FloatField()
    Pago_de_detraccion = models.BooleanField(verbose_name="Pago de detraccion")
    Documento_factura = models.FileField(verbose_name="Documento de factura", upload_to='archivos/')

    def save(self, *args, **kwargs):
        # Calcula el IGV (18% del importe)
        self.IGV = self.Importe * 0.18

        # Calcula la detracción (porcentaje de tu elección, p. ej., 10%)
        detraccion_percent = 0.10
        self.Detraccion = self.Importe * detraccion_percent

        super(factura, self).save(*args, **kwargs)

    def __str__(self):
        return f"Factura {self.id},{self.Fecha_Emision}"
