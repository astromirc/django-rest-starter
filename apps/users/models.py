from uuid import uuid7

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import MinLengthValidator
from django.db import models

from apps.shared.validators import text_validator

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(
        primary_key=True,
        default=uuid7,
        editable=False,
    )
    name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3), text_validator],
        verbose_name="Nombre",
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        error_messages={"unique": "Ya existe un usuario asociado a este email."},
    )
    password = models.CharField(
        max_length=128,
        validators=[MinLengthValidator(8)],
        verbose_name="Contraseña",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Habilitado",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Creado el",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Actualizado el",
    )

    objects = UserManager()

    # Configuración de campos
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_superuser

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        super().save(*args, **kwargs)
