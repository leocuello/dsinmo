from django import forms

from apps.property.models import Property, PropertyOperation

class SearchForm(forms.ModelForm):
    
    class Meta:
        model = Property
        fields = ['street', 'number', 'operation', 'type']