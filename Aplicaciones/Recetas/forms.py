from django import forms
from .models import Receta, Comentario

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'nombre', 'descripcion', 'ingredientes', 
            'instrucciones', 'tiempo_preparacion', 
            'nivel_dificultad', 'imagen', 'es_favorita'
        ]

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['autor', 'contenido']
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Escribe tu comentario'}),
        }
