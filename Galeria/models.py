from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nombre + " " + self.apellido
