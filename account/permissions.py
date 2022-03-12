from rest_framework.permissions import BasePermission


class CreateAccountPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'post':
            return True
        return False
