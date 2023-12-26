from django import forms
from .models import inventario

class inventarioForm(forms.ModelForm):
    class Meta:
        model = inventario
        fields = ['NombreItem', 'FechaIngreso', 'Cantidad', 'NumeroRegistro', 'Descripcion', 'TiempoVida', 'Ambiente', 'Estado']
        widgets = {
            'FechaIngreso': forms.DateInput(attrs={'type': 'date'}),
        }  