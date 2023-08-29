from django import forms
from .models import Etiqueta, Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'estado', 'etiqueta', 'observaciones']

class FiltroTareasForm(forms.Form):
    etiqueta = forms.ModelChoiceField(
        queryset=Etiqueta.objects.all(),
        empty_label='Todas las etiquetas',
        required=False
    )
    
    estado = forms.ChoiceField(
        choices=[('', 'Todos los estados')] + list(Tarea.ESTADOS),  # Agrega 'Todos los estados' como una opción
        required=False
    )

