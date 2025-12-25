from django.urls import path
from .views import (
    agenda_publica, seleccionar_fecha, seleccionar_hora, confirmar_reserva,
    mis_reservas, confirmar_cita_existente
)

urlpatterns = [
    path("", agenda_publica, name="agenda_publica"),
    path("fecha/<int:servicio_id>/", seleccionar_fecha, name="seleccionar_fecha"),
    path("horas/<int:servicio_id>/<str:fecha>/", seleccionar_hora, name="seleccionar_hora"),
    path("confirmar/<int:servicio_id>/<str:fecha>/<str:hora>/", confirmar_reserva, name="confirmar_reserva"),
    path("mis-reservas/", mis_reservas, name="mis_reservas"),
    path("confirmar-cita/<int:appointment_id>/", confirmar_cita_existente, name="confirmar_cita"),
]