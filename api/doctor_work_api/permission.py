from rest_framework.permissions import BasePermission


class Doctor_Work_permission(BasePermission):
    def has_permission(self, request, view):
        if view.action in['list','retrieve']:
            return True
        if view.action == "create":
            return request.user.is_staff
    def has_object_permission(self, request, view, obj):
        if view.action in ['update','partial_update']:
            return obj.user==request.user
        if view.action == 'destroy':
            return request.user.is_staff or request.user==obj.user