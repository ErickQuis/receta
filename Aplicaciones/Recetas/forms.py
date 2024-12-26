from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'nombre', 'descripcion', 'ingredientes', 
            'instrucciones', 'tiempo_preparacion', 
            'nivel_dificultad', 'imagen', 'es_favorita'
        ]
