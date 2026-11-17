from rest_framework.permissions import BasePermission


class Doctor_permission(BasePermission):
    def has_permission(self, request, view):
        if view.action in['list','retrieve']:
            return True
        else:
            return request.user.is_staff
    def has_object_permission(self, request, view, obj):
        if view.action in ['update','partial_update']:
            return obj.user==request.user
        if view.action == 'destroy':
            return request.user.is_staff