from django import forms
from .models import clientes
from django.core.exceptions import ValidationError

OPCIONES_TIPO_RUC = [
    ('RUC10', 'RUC10'),
    ('RUC20', 'RUC20')
]

CLIENTE_VALORACION = [
    ('Malo', 'Malo'),
    ('Bueno', 'Bueno'),
    ('Excelente','Excelente')
]

class clientesForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'  # Para incluir todos los campos del modelo en el formulario

    