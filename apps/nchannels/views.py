from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from .channel_serializer import NotificationChannelSerializer
from .channel_service import NotificationChannelService
from .container import get_channel_service
from .models import NotificationChannel


@extend_schema(tags=["channels"])
class ChannelListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    service: NotificationChannelService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_channel_service()

    def get(self, request: Request) -> Response:
        channels_list = self.service.list_channels()
        serializer = NotificationChannelSerializer(channels_list, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = NotificationChannelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        channel = NotificationChannel(**serializer.validated_data)
        created_channel = self.service.create_channel(channel)
        return Response(
            NotificationChannelSerializer(created_channel).data,
            status=HTTP_201_CREATED
        )


@extend_schema(tags=["channels"])
class ChannelDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    service: NotificationChannelService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_channel_service()

    def get(self, request: Request, channel_id: int) -> Response:
        channel = self.service.get_channel(channel_id)
        serializer = NotificationChannelSerializer(channel)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request: Request, channel_id: int) -> Response:
        serializer = NotificationChannelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        channel = self.service.get_channel(channel_id)
        channel.channel = serializer.validated_data.get('channel', channel.channel)
        channel.is_active = serializer.validated_data.get('is_active', channel.is_active)
        updated_channel = self.service.update_channel(channel_id, channel)
        return Response(NotificationChannelSerializer(updated_channel).data, status=HTTP_200_OK)

    def delete(self, request: Request, channel_id: int) -> Response:
        self.service.delete_channel(channel_id)
        return Response(status=HTTP_204_NO_CONTENT)
