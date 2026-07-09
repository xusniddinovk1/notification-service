from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from .container import get_notification_service
from .swagger.schemas import (
    list_notifications_schema,
    get_notification_by_id_schema,
    create_notification_schema,
    notification_stats_schema
)
from .serializer import (
    NotificationSerializer,
    SendNotificationSerializer
)
from .services import NotificationService


class NotificationListView(APIView):
    permission_classes = [IsAuthenticated]
    service: NotificationService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_notification_service()

    @list_notifications_schema
    def get(self, request: Request) -> Response:
        notifications = self.service.list_notifications(request.user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data, status=HTTP_200_OK)


class NotificationSendView(APIView):
    permission_classes = [IsAdminUser]
    service: NotificationService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_notification_service()

    @create_notification_schema
    def post(self, request: Request) -> Response:
        serializer = SendNotificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        template_id = serializer.validated_data["template_id"]
        payload = serializer.validated_data["payload"]
        user = request.user
        notification = self.service.create_notification(user, template_id, payload)
        return Response(
            NotificationSerializer(notification).data,
            status=HTTP_201_CREATED,
        )


class NotificationDetailView(APIView):
    permission_classes = [IsAuthenticated]
    service: NotificationService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_notification_service()

    @get_notification_by_id_schema
    def get(self, request: Request, notification_id: int) -> Response:
        notification = self.service.get_notification(request.user, notification_id)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data, status=HTTP_200_OK)


class NotificationStatsView(APIView):
    permission_classes = [IsAdminUser]

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_notification_service()

    @notification_stats_schema
    def get(self, request: Request) -> Response:
        stats = self.service.get_stats()
        return Response(stats, status=HTTP_200_OK)
