from django.shortcuts import render, redirect

from django.http import HttpResponse
from apps.search.forms import SearchForm
from apps.property.forms import ContactForm
from apps.property.models import Property, PropertyOperation

def index(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        properties = Property.objects.search(form.cleaned_data['operation'], form.cleaned_data['type'])
    else:
        properties = Property.objects.all()
    
    return render(request, 'search/index.html', {'form' : form, "properties": properties})

def view(request, id):
    property = Property.objects.get(id=id);
    if request.method == 'POST':
        form = ContactForm(request.POST) 
      
        if form.is_valid():
            contact = form.save(commit=False)
            contact.property = property
            contact.save()
        else:
            logger.error('error message')
        return redirect('success') 
    else:
         form = ContactForm() 
            
    return render(request, 'search/view.html', { 'property' : property, 'form' : form })

def success(request):
    return render(request, 'search/success.html')


