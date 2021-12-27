from rest_framework.permissions import BasePermission,SAFE_METHODS

class MyPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("=====================================================")
        if request.Method in SAFE_METHODS:
            print(request.user)
            if request.user ==obj.owner:
                return True
        return False

