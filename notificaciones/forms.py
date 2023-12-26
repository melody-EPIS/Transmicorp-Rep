from django import forms
from .models import notificacion

class NotificacionesForm(forms.ModelForm):
    class Meta:
        model = notificacion
        fields = '__all__'  # Para incluir todos los campos del modelo en el formulario