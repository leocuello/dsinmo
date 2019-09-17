from django.db import models
# Create your models here.

class PropertyType(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return "%s" % (self.name)

class PropertyOperation(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return "%s" % (self.name)

class PropertyManager(models.Manager):
    def search(self, operation, type):
        return self.filter(operation=operation).filter(type=type)

class Property(models.Model):
    street = models.CharField(max_length = 50)
    number = models.IntegerField()
    operation = models.ForeignKey(PropertyOperation, on_delete=models.CASCADE)
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    objects = PropertyManager()

    def __str__(self):
        return "%s %s" % (self.street, self.number)

class Contact(models.Model):
    name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    message = models.CharField(max_length = 200)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

