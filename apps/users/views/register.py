from ..swagger.schemas import register_user_schema
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.users.serializers.register import RegisterSerializer
from ..throttles import RegisterRateThrottle


class RegisterView(APIView):
    throttle_classes = [RegisterRateThrottle]

    @register_user_schema
    def post(self, request: Request) -> Response:
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
