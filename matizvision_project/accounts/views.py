from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import logout


# =======================
#  REGISTER VIEW 
# =======================
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tu cuenta fue creada exitosamente. Ahora puedes iniciar sesión.")
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


# =======================
#  LOGIN VIEW 
# =======================
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            # CustomUser usa email como username
            user = authenticate(request, username=email, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Has iniciado sesión correctamente.")
                    # return redirect("home")
                else:
                    messages.error(request, "Tu cuenta está inactiva. Contacta a la óptica.")
            else:
                messages.error(request, "Credenciales inválidas. Revisa correo y contraseña.")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


# =======================
#  LOGOUT VIEW
# =======================
def logout_view(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect("login")