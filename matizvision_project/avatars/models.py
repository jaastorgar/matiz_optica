from django.db import models

AVATAR_TIPOS = [
    ("static", "Estático"),
    ("animated", "Animado"),
]

SECCIONES = [
    ("home", "Home"),
    ("tienda", "Tienda"),
    ("agenda", "Agenda Médica"),
    ("perfil", "Perfil del Usuario"),
    ("general", "General"),
]

class Avatar(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=AVATAR_TIPOS, default="static")
    imagen = models.ImageField(upload_to="avatars/static/", blank=True, null=True)
    archivo_animado = models.FileField(upload_to="avatars/animados/", blank=True, null=True)
    descripcion = models.TextField(blank=True)
    seccion = models.CharField(max_length=20, choices=SECCIONES, default="general")
    activo = models.BooleanField(default=True)
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre