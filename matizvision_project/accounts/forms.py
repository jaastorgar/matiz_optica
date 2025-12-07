from django import forms
from .models import CustomUser, Profile


class RegisterForm(forms.ModelForm):
    # Campos adicionales que NO están en CustomUser
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput()
    )

    run = forms.CharField(max_length=8)
    dv = forms.CharField(max_length=1)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))

    region = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    comuna = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = [
            "full_name",
            "email",
            "phone",
        ]

    def save(self, commit=True):
        # Crear usuario base
        user = CustomUser(
            email=self.cleaned_data["email"],
            full_name=self.cleaned_data["full_name"],
            phone=self.cleaned_data["phone"],
        )

        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()

            # El Profile se crea automáticamente con signals
            profile = user.profile

            # Datos del Profile
            profile.run = self.cleaned_data["run"]
            profile.dv = self.cleaned_data["dv"]
            profile.birth_date = self.cleaned_data["birth_date"]
            profile.region = self.cleaned_data["region"]
            profile.city = self.cleaned_data["city"]
            profile.comuna = self.cleaned_data["comuna"]
            profile.address = self.cleaned_data["address"]

            profile.save()

        return user

class LoginForm(forms.Form):

    email = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            "placeholder": "correo@ejemplo.cl"
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Ingresa tu contraseña"
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)