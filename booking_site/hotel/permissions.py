from rest_framework import permissions

class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and not request.user.is_staff


class IsNotHotelOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and not request.user.is_staff