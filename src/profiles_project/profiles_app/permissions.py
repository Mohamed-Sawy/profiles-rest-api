from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """allow viewing other users but only update your own user"""

        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.id
