from rest_framework import permissions


class IsCustomer(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Customer').exists():
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if request.user.groups.filter(name='Customer').exists():
            return True
        else:
            return False