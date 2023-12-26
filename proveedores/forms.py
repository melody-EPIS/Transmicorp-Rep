from django import forms
from .models import Proveedor

class CustomTextInputWidget(forms.TextInput):
    input_type = 'text'  # Cambia el tipo de entrada a "text"

class proveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'

    # Personaliza el widget del campo de correo electrónico
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Correo'].widget = CustomTextInputWidget()
