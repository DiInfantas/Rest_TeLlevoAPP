from django.db import models

# Create your models here.

class Viaje(models.Model):
    hora_salida = models.TimeField( verbose_name="Hora de salida")
    lugarInicio = models.CharField(max_length=30,  verbose_name="Lugar inicio")
    lugarDestino = models.CharField(max_length=30,  verbose_name="Destino Viaje")
    precio = models.PositiveIntegerField( verbose_name="Precio")

    def __str__(self):
        return f"desde {self.lugarInicio} a {self.lugarDestino} a las {self.hora_salida}"
    