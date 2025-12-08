from django.contrib import admin
from .models import Avatar

@admin.register(Avatar)
class AvatarAdmin(admin.ModelAdmin):
    list_display = ("nombre", "tipo", "seccion", "activo", "creado")
    list_filter = ("tipo", "seccion", "activo")
    search_fields = ("nombre", "descripcion")
    ordering = ("-creado",)