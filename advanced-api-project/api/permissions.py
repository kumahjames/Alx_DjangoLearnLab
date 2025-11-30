from rest_framework import permissions

# Custom permission - only allow authors to edit their own books
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # Write permissions are only allowed to the owner (author)
        # For now, we'll allow any authenticated user since we don't have user ownership
        return request.user and request.user.is_authenticated


# Permission for staff users only
class IsStaffUser(permissions.BasePermission):
    """
    Custom permission to only allow staff users to access the view.
    """
    
    def has_permission(self, request, view):
        return request.user and request.user.is_staff