from django.urls import path

from apps.search.views import index, view, success

urlpatterns = [
    path('', index, name='index'),
    path('view/<int:id>', view, name='view'),
    path('success', success, name='success'),
]
