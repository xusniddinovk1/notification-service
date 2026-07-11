from rest_framework.permissions import (
    BasePermission,
    IsAuthenticated,
    IsAdminUser,
    SAFE_METHODS,
)
from rest_framework.request import Request
from rest_framework.views import APIView


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request: Request, view: APIView) -> bool:
        if request.method in SAFE_METHODS:
            return IsAuthenticated().has_permission(request, view)
        return IsAdminUser().has_permission(request, view)
