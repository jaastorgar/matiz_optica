from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import AppointmentService, Appointment
from django.contrib import messages
from datetime import datetime, time


# 1️⃣ Ver agenda pública (servicios)
def agenda_publica(request):
    servicios = AppointmentService.objects.all()
    return render(request, "appointments/agenda_publica.html", {"servicios": servicios})


# 2️⃣ Seleccionar fecha
def seleccionar_fecha(request, servicio_id):
    servicio = AppointmentService.objects.get(id=servicio_id)
    return render(request, "appointments/seleccionar_fecha.html", {"servicio": servicio})


# 3️⃣ Seleccionar horario disponible
def seleccionar_hora(request, servicio_id, fecha):
    servicio = AppointmentService.objects.get(id=servicio_id)

    # Horarios fijos básicos (8 opciones)
    horarios_base = [
        "09:00", "09:30",
        "10:00", "10:30",
        "11:00", "11:30",
        "12:00", "12:30",
    ]

    # Obtener ocupadas
    ocupadas = Appointment.objects.filter(servicio=servicio, fecha=fecha).values_list("hora", flat=True)
    ocupadas = [h.strftime("%H:%M") for h in ocupadas]

    # Filtrar
    disponibles = [h for h in horarios_base if h not in ocupadas]

    return render(request, "appointments/seleccionar_hora.html", {
        "servicio": servicio,
        "fecha": fecha,
        "horarios": disponibles
    })


# 4️⃣ Confirmar reserva (requiere login)
@login_required
def confirmar_reserva(request, servicio_id, fecha, hora):
    servicio = AppointmentService.objects.get(id=servicio_id)

    # Validación simple
    ya_ocupada = Appointment.objects.filter(servicio=servicio, fecha=fecha, hora=hora).exists()
    if ya_ocupada:
        messages.error(request, "La hora ya fue tomada.")
        return redirect("seleccionar_hora", servicio_id=servicio_id, fecha=fecha)

    Appointment.objects.create(
        user=request.user,
        servicio=servicio,
        fecha=fecha,
        hora=hora,
    )

    messages.success(request, "Reserva confirmada exitosamente.")
    return redirect("agenda_publica")