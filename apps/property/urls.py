from django.urls import path

from apps.property.views import index, create, update

urlpatterns = [
    path('', index, name='index'),
    path('create', create, name='create'),
    path('update/<int:id>', update, name='update'),
]
