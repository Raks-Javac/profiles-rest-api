from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):

    def has_object_permission(self,request,view,obj):
        """This method checks for users trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True


        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission):
    """This checks if users want to update their own status"""

    def has_object_permission(self,request,view,obj):
        """This methods provides the check logic to the PostOwnStatus class"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
