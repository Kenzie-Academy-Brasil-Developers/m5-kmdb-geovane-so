from rest_framework import permissions

class IsReviewPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS: return True

        if (
            request.user and 
            request.user.is_authenticated and 
            request.user.is_superuser
        ): 
            return True

        if (
            request.user and 
            request.user.is_authenticated and 
            request.user.is_critic
        ): 
            return True
        
        return False
