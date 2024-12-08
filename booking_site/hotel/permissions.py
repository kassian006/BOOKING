from rest_framework import permissions


class CheckBooking(permissions.BasePermission):
    def has_permission(self, request, view):
            if request.user.status == 'customer':
                return True
            return False

class UseCRUD(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user ==  obj.owner:
            return True
        return False

class CreateReview(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'customer':
            return True
        return False
