from django import forms
from .models import clientes, clienteRUC10, clienteRUC20
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

#FORMS PARA RUC 10 y RUC 20 -> TIPOS DE CLIENTES
class ClienteRUC10Form(forms.ModelForm):
    class Meta:
        model = clienteRUC10
        fields = '__all__'

class ClienteRUC20Form(forms.ModelForm):
    class Meta:
        model = clienteRUC20
        fields = '__all__'

