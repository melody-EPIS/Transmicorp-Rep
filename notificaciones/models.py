from django.db import models
from inventario.models import inventario
class notificacion(models.Model):
    Id_notificaciones = models.CharField(max_length=12)
    Inventario = models.ForeignKey(inventario, on_delete=models.CASCADE) # relacion uno a mucho con la tabla inventario
    Evento = models.CharField(max_length=12)
    Descripcion = models.TextField()

    def __str__(self):
        return f"Notificacion {self.id}"
