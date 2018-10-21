from django import forms
from persona.models import Persona

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = [
            'id_persona',
            'nombre',
        ]

        labels = {
            'id_persona': 'id',
            'nombre': 'Nombre',
        }

        widgets = {
            'id_persona' : forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'})

        }
