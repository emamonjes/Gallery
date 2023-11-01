from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'contraseña', 'email']

    # Puedes agregar validaciones personalizadas u otros campos si es necesario
    # Por ejemplo, si quieres agregar una confirmación de contraseña:
    confirmar_contraseña = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get('contraseña')
        confirmar_contraseña = cleaned_data.get('confirmar_contraseña')

        if contraseña != confirmar_contraseña:
            raise forms.ValidationError("Las contraseñas no coinciden. Por favor, inténtelo de nuevo.")

