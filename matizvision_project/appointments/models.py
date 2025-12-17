from django.db import models
from django.conf import settings


class AppointmentService(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Appointment(models.Model):
    ESTADOS = [
        ("reagendar", "Reagendar"),
        ("pendiente", "Pendiente"),
        ("confirmada", "Confirmada"),
        ("cancelada", "Cancelada"),
        ("atendida", "Atendida"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    servicio = models.ForeignKey(AppointmentService, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default="pendiente")
    creado = models.DateTimeField(auto_now_add=True)