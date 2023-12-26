from django import forms
from .models import unidades

class unidadesForm(forms.ModelForm):
    class Meta:
        model = unidades
        fields = '__all__'  # Para incluir todos los campos del modelo en el formulario

    