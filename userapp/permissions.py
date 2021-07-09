from rest_framework import authentication, permissions
class DataOwner(permissions.BasePermission):
    # for view permission
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    # for object level permissions
    def has_object_permission(self, request, view, user_obj):
        return user_obj.id== request.user.id