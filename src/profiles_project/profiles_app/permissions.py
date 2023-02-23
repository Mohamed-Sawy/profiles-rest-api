from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """allow viewing other users but only update your own user"""

        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.id == obj.id


class PostOwnStatus(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """allow viewing other statuses but only update your own status"""

        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile.id == request.user.id
