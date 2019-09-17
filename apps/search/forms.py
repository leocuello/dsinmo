from django import forms

from apps.property.models import Property, PropertyOperation, PropertyType

class SearchForm(forms.Form):

    operation = forms.ModelChoiceField(queryset=PropertyOperation.objects.all(), required=False, widget = forms.Select(attrs = {'class':"form-control"}))

    type = forms.ModelChoiceField(queryset=PropertyType.objects.all(), required=False, widget = forms.Select(attrs = {'class':"form-control"}))