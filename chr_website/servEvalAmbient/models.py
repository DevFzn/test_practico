from django.db import models

# Nota: Los valores máximos admitidos deben ser optimizados.

class Empresa(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=1000)
    tipo = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    tipologia = models.CharField(max_length=255)
    titular = models.CharField(max_length=255)
    inversion = models.CharField(max_length=255)
    fecha = models.DateField()
    estado = models.CharField(max_length=255)
    mapa = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

