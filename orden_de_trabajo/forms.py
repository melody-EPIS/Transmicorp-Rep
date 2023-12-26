
from django import forms
from .models import Orden_trabajo

OPCIONES_TIPO_ORDEN =[
       ('No tercerizada', 'No tercerizada'),
       ('Tercerizada', 'Tercerizada')
]

class OrdenTrabajoForm(forms.ModelForm):
    class Meta:
        model = Orden_trabajo
        #fields = '__all__'  # Para incluir todos los campos del modelo en el formulario
        fields = ('Cliente', 'Id_Conductor', 'Id_Vehiculo', 'Origen', 'Destino', 'Detalles', 'Peso', 'Fecha_Emision', 'Descripcion','Monto_Cotizacion', 'Estado', 'Tipo_orden_de_trabajo')
        widgets = {
           'Fecha_Emision': forms.DateInput(attrs={'type': 'date'}),
           'Tipo_orden_de_trabajo': forms.RadioSelect(attrs={'class': 'tipo-orden-radio'}),
           'Estado': forms.CheckboxInput(attrs={'class': 'custom-checkbox'}),
           'Detalles': forms.Textarea(attrs={'cols': 27, 'rows': 4}),
           'Descripcion': forms.Textarea(attrs={'cols': 62, 'rows': 5}),
        }
   
    def __init__(self, *args, **kwargs): 
        super(OrdenTrabajoForm, self).__init__(*args, **kwargs)
        self.fields['Tipo_orden_de_trabajo'].choices = OPCIONES_TIPO_ORDEN