from django.urls import path

from apps.search.views import index

urlpatterns = [
    path('', index, name='index'),
]
