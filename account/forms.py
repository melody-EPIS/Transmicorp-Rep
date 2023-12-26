from django import forms
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

class CustomPasswordChangeForm(PasswordChangeForm):
    new_password2 = forms.CharField(label='Confirmar nueva contraseña', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")
        print("Contraseña cambiada con éxito")

        if new_password and new_password2 and new_password != new_password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        print("Contraseña cambiada con éxito")

        return cleaned_data