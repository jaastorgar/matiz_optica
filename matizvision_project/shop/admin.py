from django.contrib import admin
from .models import Categoria, Producto


# =============================
#   CATEGORÍA
# =============================
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "slug")
    search_fields = ("nombre",)
    prepopulated_fields = {"slug": ("nombre",)}
    ordering = ("nombre",)


# =============================
#   PRODUCTO
# =============================
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "stock", "mostrar_imagen")
    list_filter = ("categoria",)
    search_fields = ("nombre", "descripcion")
    prepopulated_fields = {"slug": ("nombre",)}
    ordering = ("nombre",)

    # Mostrar imagen en admin (miniatura)
    def mostrar_imagen(self, obj):
        if obj.imagen:
            return f'<img src="{obj.imagen.url}" width="60" style="border-radius:6px;" />'
        return "(Sin imagen)"
    mostrar_imagen.allow_tags = True
    mostrar_imagen.short_description = "Imagen"