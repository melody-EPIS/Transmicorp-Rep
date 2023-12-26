from django import forms
from .models import gastos

class GastosForm(forms.ModelForm):
    class Meta:
        model = gastos
        fields = ('Factura', 'Orden_de_trabajo', 'Inventario', 'Codigo_de_boleta', 'Tipo_de_gasto', 'Area_de_gasto', 'Descripcion','Fecha_boleta', 'Monto_gastado', 'Documento_boleta')
        widgets = {
           'Fecha_boleta': forms.DateInput(attrs={'type': 'date'}),
        }