from django.db import models


# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()


class PropertyImages(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="PropertyImages/")
