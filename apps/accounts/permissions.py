from rest_framework.permissions import BasePermission

class IsEditor(BasePermission):
    """
    Permite el acceso solo a usuarios con el rol de Editor.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == "editor"

class IsPeriodista(BasePermission):
    """
    Permite acceso solo a los editores con sub-rol 'periodista'.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "editor" and
            request.user.sub_role == "periodista"
        )

class IsGestorActividades(BasePermission):
    """
    Permite acceso solo a los editores con sub-rol 'gestor de actividades'.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "editor" and
            request.user.sub_role == "gestor_actividades"
        )

class IsFotografo(BasePermission):
    """
    Permite acceso solo a los editores con sub-rol 'fotógrafo'.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "editor" and
            request.user.sub_role == "fotografo"
        )
