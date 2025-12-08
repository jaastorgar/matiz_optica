from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Avatar

def obtener_avatar(request, seccion):
    avatar = Avatar.objects.filter(seccion=seccion, activo=True).order_by("-creado").first()

    if not avatar:
        return JsonResponse({"error": "No hay avatares disponibles"}, status=404)

    return JsonResponse({
        "nombre": avatar.nombre,
        "tipo": avatar.tipo,
        "descripcion": avatar.descripcion,
        "imagen": avatar.imagen.url if avatar.imagen else None,
        "animado": avatar.archivo_animado.url if avatar.archivo_animado else None,
    })