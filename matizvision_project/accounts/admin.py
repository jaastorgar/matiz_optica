from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile


# ============================
#   INLINE DEL PERFIL
# ============================
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    extra = 0
    fields = (
        "run", "dv", "birth_date",
        "region", "city", "comuna", "address"
    )


# ============================
#   CUSTOM USER ADMIN
# ============================
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = (
        "email",
        "full_name",
        "phone",
        "role",
        "is_active",
        "is_staff",
    )

    list_filter = (
        "role",
        "is_active",
        "is_staff",
    )

    search_fields = (
        "email",
        "full_name",
        "phone",
        "profile__run",
    )

    ordering = ("email",)

    # Campos que se muestran en la vista de edición
    fieldsets = (
        ("Información de Usuario", {
            "fields": ("email", "full_name", "phone", "password")
        }),
        ("Permisos", {
            "fields": ("role", "is_active", "is_staff", "is_superuser")
        }),
        ("Fechas importantes", {
            "fields": ("last_login",)
        }),
    )

    # Campos necesarios en la creación
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "full_name",
                "phone",
                "role",
                "password1",
                "password2",
                "is_active",
                "is_staff",
            ),
        }),
    )

    inlines = [ProfileInline]


# ============================
#   PERFIL
# ============================
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "run",
        "dv",
        "birth_date",
        "region",
        "comuna",
    )

    search_fields = (
        "user__email",
        "user__full_name",
        "run",
        "comuna",
        "region",
    )

    list_filter = (
        "region",
        "comuna",
    )