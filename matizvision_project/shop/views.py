from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Categoria
from avatars.models import Avatar


def shop_home(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    avatar = Avatar.objects.filter(
        activo=True,
        seccion="tienda"
    ).first()

    return render(
        request,
        "shop/home.html",
        {
            "productos": productos,
            "categorias": categorias,
            "avatar": avatar,
        }
    )


def product_detail(request, slug):
    producto = get_object_or_404(Producto, slug=slug)

    # ✅ SOLO RESPONDE A PETICIONES AJAX (MODAL)
    if request.headers.get("x-requested-with") == "XMLHttpRequest":
        return render(request, "shop/detail.html", {
            "producto": producto,
        })

    # ❌ SI NO ES AJAX → NUNCA RENDERIZA detail.html
    return redirect("shop_home")