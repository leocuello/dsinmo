from django.shortcuts import render, redirect

from django.http import HttpResponse
from apps.search.forms import SearchForm
from apps.property.models import PropertyOperation

def index(request):
    if(request.method == 'GET'):
        form = SearchForm(request.GET)
        if form.is_valid():
            form.save()
    
    else:
        form = PropertyForm()

    return render(request, 'search/index.html', {'form' : form})
