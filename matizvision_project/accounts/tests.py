from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import CustomUser, Profile
from accounts.forms import RegisterForm


class UserModelTests(TestCase):

    def test_create_user(self):
        """Debe crear un usuario correctamente usando CustomUser"""
        user = CustomUser.objects.create_user(
            email="test@example.com",
            password="12345678",
            full_name="Usuario Test",
            phone="912345678"
        )

        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("12345678"))
        self.assertEqual(user.role, "CLIENT")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        """Debe crear un superusuario con los permisos correctos"""
        admin = CustomUser.objects.create_superuser(
            email="admin@example.com",
            password="12345678"
        )

        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        self.assertEqual(admin.role, "ADMIN")

    def test_profile_auto_created(self):
        """Al crear un CustomUser, su Profile debe generarse automáticamente."""
        user = CustomUser.objects.create_user(
            email="auto@profile.com",
            password="12345678"
        )

        profile = Profile.objects.get(user=user)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.user.email, "auto@profile.com")


class RegisterFormTests(TestCase):

    def test_register_form_saves_user(self):
        """El formulario debe crear un usuario y su perfil correctamente."""

        form_data = {
            "full_name": "Juan Pérez",
            "email": "juan@example.com",
            "phone": "987654321",
            "password1": "abcdef12",
            "password2": "abcdef12",
            "run": "12345678",
            "dv": "K",
            "birth_date": "1999-05-10",
            "region": "Región Metropolitana",
            "city": "Santiago",
            "comuna": "Providencia",
            "address": "Av. Siempre Viva 123",
        }

        form = RegisterForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

        user = form.save()

        # Revisar usuario
        self.assertEqual(user.email, "juan@example.com")
        self.assertTrue(user.check_password("abcdef12"))

        # Revisar profile
        profile = user.profile
        self.assertEqual(profile.run, "12345678")
        self.assertEqual(profile.dv, "K")
        self.assertEqual(profile.region, "Región Metropolitana")
        self.assertEqual(profile.address, "Av. Siempre Viva 123")


class RegisterViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_register_view_renders(self):
        """La vista de registro debe cargar correctamente la página."""
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/register.html")

    def test_register_view_creates_user(self):
        """La vista debe procesar el formulario y crear un usuario."""
        response = self.client.post(reverse("register"), {
            "full_name": "Mario Test",
            "email": "mario@example.com",
            "phone": "987654321",
            "password1": "abc12345",
            "password2": "abc12345",
            "run": "23456789",
            "dv": "5",
            "birth_date": "2000-01-01",
            "region": "Región Metropolitana",
            "city": "Santiago",
            "comuna": "Ñuñoa",
            "address": "Calle Ejemplo 321"
        })

        # Después de un registro exitoso debería redirigir al login
        self.assertEqual(response.status_code, 302)

        # Verificar que se creó el usuario
        self.assertTrue(CustomUser.objects.filter(email="mario@example.com").exists())

        # Verificar Profile
        user = CustomUser.objects.get(email="mario@example.com")
        self.assertEqual(user.profile.comuna, "Ñuñoa")