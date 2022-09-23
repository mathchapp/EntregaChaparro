from django.db import models

# Create your models here.

class Familiares(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fechaNac = models.DateField()

class Liga(models.Model):
    nombre = models.CharField(max_length=60)
    pais = models.CharField(max_length=60)
    division = models.CharField(max_length=60)

class Jugador(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    edad = models.IntegerField()
    puesto = models.CharField(max_length=60)

class Equipo(models.Model):
    nombre = models.CharField(max_length=60)
    procedencia = models.CharField(max_length=60)
    division = models.CharField(max_length=60)
    


