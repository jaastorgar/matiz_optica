from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

# ============================
#  CUSTOM USER MANAGER
# ============================
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Crear usuario normal usando email como identificador"""
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Crear superusuario con privilegios administrativos"""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("role", "ADMIN")

        if extra_fields.get("is_staff") is not True:
            raise ValueError("El superusuario debe tener is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("El superusuario debe tener is_superuser=True")

        return self.create_user(email, password, **extra_fields)

# ============================
#        CUSTOM USER
# ============================
class CustomUser(AbstractBaseUser, PermissionsMixin):

    # ---- ROLES DEL SISTEMA ----
    ROLE_CHOICES = [
        ('CLIENT', 'Cliente'),
        ('STAFF', 'Staff de Óptica'),
        ('ADMIN', 'Administrador'),
    ]

    # ---- CAMPOS BÁSICOS ----
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    # ---- ROL DEL USUARIO ----
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='CLIENT'
    )

    # ---- ESTADOS ----
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    # ---- MANAGER ----
    objects = CustomUserManager()

    # ---- LOGIN POR EMAIL ----
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

# ============================
#        PROFILE
# ============================
class Profile(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    # ---- DATOS PERSONALES ----
    run = models.CharField(max_length=8, blank=True)  # solo números, sin DV
    dv = models.CharField(max_length=1, blank=True)   # dígito verificador
    birth_date = models.DateField(null=True, blank=True)

    # ---- DIRECCIÓN ----
    region = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    comuna = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=255, blank=True)

    # ---- AVATAR ANIMADO ----
    avatar_path = models.CharField(
        max_length=255,
        blank=True,
        help_text="Ruta del archivo JSON de Lottie para el avatar animado."
    )

    # ---- INFO ADICIONAL ----
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Perfil de {self.user.email}"

# ============================
#      SIGNALS (AUTOCREATE)
# ============================
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """Crear un Profile automáticamente cuando se crea un CustomUser"""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    """Guardar el perfil automáticamente al guardar el usuario"""
    instance.profile.save()