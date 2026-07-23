from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeForm, UserCreationForm
from .models import User

# Oculta el modelo Groups del admin
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        "name",
        "email",
        "is_superuser",
        "is_active",
        "created_at",
    ]
    search_fields = ["name", "email"]
    list_filter = ["is_superuser", "is_active"]
    ordering = ["-created_at"]
    readonly_fields = [
        "id",
        "last_login",
        "created_at",
        "updated_at",
    ]
    exclude = ["groups", "user_permissions"]

    fieldsets = (
        ("Credenciales", {"fields": ["email", "password"]}),
        (
            "Información general",
            {
                "fields": [
                    "name",
                    "is_active",
                    "is_superuser",
                    "last_login",
                    "created_at",
                    "updated_at",
                ],
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ["email", "name", "password1", "password2"],
            },
        ),
    )

    # Deshabilita la acción de eliminar usuarios desde el admin
    def has_delete_permission(self, _request, _obj=None):
        return False
