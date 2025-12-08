from django.db import models
from django.conf import settings


class AppointmentService(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    servicio = models.ForeignKey(AppointmentService, on_delete=models.CASCADE)

    fecha = models.DateField()
    hora = models.TimeField()

    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.servicio.nombre} - {self.fecha} {self.hora}"