from django.shortcuts import render, get_object_or_404
from .models import Producto, Categoria


def shop_home(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()

    return render(request, "shop/home.html", {
        "productos": productos,
        "categorias": categorias,
    })


def product_detail(request, slug):
    producto = get_object_or_404(Producto, slug=slug)

    return render(request, "shop/detail.html", {
        "producto": producto,
    })