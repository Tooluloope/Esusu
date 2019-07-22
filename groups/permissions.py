from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the Creator of this Group'
    def has_object_permission(self, request, view, obj):

        return obj.created_by == request.user