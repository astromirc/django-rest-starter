from django.core.validators import RegexValidator

# Letras, números, puntos, guiones y comas.
text_validator = RegexValidator(
    regex=r"^[a-zA-ZñáéíóúÑÁÉÍÓÚ0-9 \.\-\,]+$",
    message="Solo se permiten letras, números, puntos, guiones y comas.",
)
