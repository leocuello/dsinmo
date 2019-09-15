from django import forms

from apps.property.models import Property

class PropertyForm(forms.ModelForm):
    
    class Meta:
        model = Property

        fields = [
             'street',
             'number',
             'operation',
             'type',
        ]
        labels = {
            'street': 'Calle',
            'number': 'Número',
            'operation': 'Operación',
            'type': 'Tipo',
        }
        widgets = {
            'street': forms.TextInput(attrs={'class':'form-control'}),
            'number': forms.TextInput(attrs={'class':'form-control'}),
            'operation': forms.Select(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}),
        }
