from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fechaDeNac = models.DateField()
