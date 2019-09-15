from django.shortcuts import render, redirect

from apps.property.forms import PropertyForm
from apps.property.models import Property
import logging
logger = logging.getLogger(__name__)


def index(request):
    properties = Property.objects.all();
    context = {'properties': properties }
    return render(request, 'property/index.html', context)

def update(request, id):
    property = Property.objects.get(id=id);
    if request.method == 'GET':
        form = PropertyForm(instance=property) 
    else:
        form = PropertyForm(request.POST, instance=property) 
        if form.is_valid():
            form.save()
        else:
            logger.error('error message')
        return redirect('index')     
    return render(request, 'property/create.html', { 'form' : form })
    
def create(request):
    if(request.method == 'POST'):
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            logger.error(form.errors)
        return redirect('index')
    else:
        form = PropertyForm()
    return render(request, 'property/create.html', {'form' : form})