from django.contrib import admin

from apps.property.models import Property, PropertyType, PropertyOperation, Contact

# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyType)
admin.site.register(PropertyOperation)
admin.site.register(Contact)