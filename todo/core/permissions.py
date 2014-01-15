# coding: utf-8
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Permissão customizada para permitir que somente donos de um objeto possam editá-lo.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user


class IsOwner(permissions.BasePermission):
    """
    Permissão customizada para permitir que somente donos de um objeto possam editá-lo.
    """

    def has_object_permission(self, request, view, obj):
        # Permissions are only allowed to the owner of the task.
        return obj.owner == request.user