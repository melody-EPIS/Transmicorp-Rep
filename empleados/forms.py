from django import forms
from .models import Empleados
from django.core.exceptions import ValidationError

OPCIONES_ESTADO_LICENCIA =[
    ('1','Vigente'),
    ('2','Suspendida'),
    ('3','Vencida'),
    ('4','Invalida')
]

TIPO_LICENCIA =[
        ('1','A-I'),
        ('2','A-IIa'),
        ('3','A-IIb'),
        ('4','A-IIIa'),
        ('5','A-IIIb'),
        ('6','A-IIIc'),
        ('7','B-I'),
        ('8','B-IIa'),
        ('9','B-IIb'),
        ('10','B-IIc')
]

OPCIONES_RENDIMIENTO = [
    ('1', 'Excelente'),
    ('2', 'Bueno'),
    ('3', 'Regular'),
    ('4', 'Necesita Mejorar'),
    ('5', 'Deficiente.'),
]

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = '__all__'  # Para incluir todos los campos del modelo en el formulario

    Estado_Licencia = forms.ChoiceField(choices=OPCIONES_ESTADO_LICENCIA)
    