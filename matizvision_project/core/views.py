from django.shortcuts import render
from avatars.models import Avatar

# Create your views here.
def home_view(request):
    avatar = Avatar.objects.filter(
        activo=True,
        seccion="general"
    ).first()

    return render(request, "core/home.html", {
        "avatar": avatar
    })