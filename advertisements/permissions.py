from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated


class AdvertisementPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        if request.method == 'GET':
            return True
        return request.user.is_authenticated

        
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method == 'GET':
            return True
        return request.user == obj.creator
