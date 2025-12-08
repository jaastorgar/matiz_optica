from django.urls import path
from .views import agenda_publica, seleccionar_fecha, seleccionar_hora, confirmar_reserva

urlpatterns = [
    path("", agenda_publica, name="agenda_publica"),
    path("fecha/<int:servicio_id>/", seleccionar_fecha, name="seleccionar_fecha"),
    path("horas/<int:servicio_id>/<str:fecha>/", seleccionar_hora, name="seleccionar_hora"),
    path("confirmar/<int:servicio_id>/<str:fecha>/<str:hora>/", confirmar_reserva, name="confirmar_reserva"),
]