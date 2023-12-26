from django.db import models

# Create your models here.
class inventario(models.Model):
    Id_Inventario = models.AutoField(primary_key=True)
    NombreItem = models.CharField(max_length=100)
    FechaIngreso = models.DateField()
    Cantidad = models.IntegerField()
    NumeroRegistro = models.IntegerField()
    Descripcion = models.CharField(max_length=100)
    TiempoVida = models.IntegerField()
    Ambiente = models.FileField(upload_to='archivos/')
    Estado = models.BooleanField()

    def __str__(self):
        return f"inventario {self.NombreItem}"