from drf_spectacular.utils import extend_schema
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from apps.users.serializers.register import RegisterSerializer


@extend_schema(request=RegisterSerializer, responses=RegisterSerializer)
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, tokens = serializer.save()
        return Response(
            {
                "users": RegisterSerializer(user).data,
                "tokens": tokens,
            },
            status=status.HTTP_201_CREATED,
        )
