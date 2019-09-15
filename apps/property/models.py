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

class Property(models.Model):
    street = models.CharField(max_length = 50)
    number = models.IntegerField()
    operation = models.ForeignKey(PropertyOperation, on_delete=models.CASCADE)
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.street, self.number)
