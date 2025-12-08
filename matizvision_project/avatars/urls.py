from django.urls import path
from .views import obtener_avatar

urlpatterns = [
    path("get/<str:seccion>/", obtener_avatar, name="obtener_avatar"),
]