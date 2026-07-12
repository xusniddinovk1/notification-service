from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from ..container import get_notification_service
from ..serializers.bulk_notification import BulkSendNotificationSerializer
from ..serializers.notification import NotificationSerializer
from ..services import NotificationService


class BulkSendNotificationView(APIView):
    permission_classes = (IsAdminUser,)
    service: NotificationService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_notification_service()

    def post(self, request: Request) -> Response:
        serializer = BulkSendNotificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        users_id = serializer.validated_data["user_ids"]
        template_id = serializer.validated_data["template_id"]
        payload = serializer.validated_data["payload"]

        notifications = self.service.bulk_create_notifications(
            users_id, template_id, payload
        )
        return Response(
            NotificationSerializer(notifications, many=True).data,
            status=status.HTTP_201_CREATED,
        )
