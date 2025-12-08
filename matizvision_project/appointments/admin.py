from django.contrib import admin
from .models import AppointmentService, Appointment


# ===============================
#    ADMIN DE SERVICIOS
# ===============================
@admin.register(AppointmentService)
class AppointmentServiceAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)
    ordering = ("nombre",)


# ===============================
#    ADMIN DE RESERVAS
# ===============================
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "servicio",
        "fecha",
        "hora",
        "creado",
    )

    list_filter = (
        "servicio",
        "fecha",
    )

    search_fields = (
        "user__email",
        "user__full_name",
        "servicio__nombre",
    )

    ordering = ("-fecha", "-hora")