from django import forms

from apps.property.models import Property, Contact

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

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact

        fields = [
             'name',
             'email',
             'message',
        ]
        labels = {
            'name': 'Nombre',
            'email': 'Email',
            'message': 'Mensaje',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'cols': 20, 'rows': 6, 'class':'form-control'}),
        }
