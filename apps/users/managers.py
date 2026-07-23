from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, name, email, password, **extra_fields):
        if not email:
            raise ValueError("El email es obligatorio.")

        user = self.model(name=name, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(name, email, password, **extra_fields)
