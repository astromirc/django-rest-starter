from rest_framework.permissions import BasePermission


class DenyAll(BasePermission):
    """
    Deniega acceso por defecto a todas las vistas.
    Obliga a especificar permisos explícitos en cada vista que requiera acceso.
    """

    def has_permission(self, _request, _view):
        return False

    def has_object_permission(self, _request, _view, _obj):
        return False
