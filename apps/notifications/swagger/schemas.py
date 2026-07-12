from rest_framework import serializers

from ..serializers.bulk_notification import BulkSendNotificationSerializer
from ..serializers.notification import NotificationSerializer, SendNotificationSerializer
from drf_spectacular.utils import extend_schema, inline_serializer

list_notifications_schema = extend_schema(
    summary="List of notifications",
    description="List of notifications",
    responses={200: NotificationSerializer(many=True)},
    tags=["notifications"],
)

get_notification_by_id_schema = extend_schema(
    summary="Get a notification",
    description="Get a notification by its id",
    responses={200: NotificationSerializer()},
    tags=["notifications"],
)

create_notification_schema = extend_schema(
    summary="Send a new notification",
    description="Send a notification to a user. Admin only.",
    request=SendNotificationSerializer,
    responses={201: NotificationSerializer()},
    tags=["notifications"],
)

notification_stats_schema = extend_schema(
    summary="Get notification stats",
    description="Returns delivery statistics. Admin only.",
    responses={
        200: inline_serializer(
            name="NotificationStats",
            fields={
                "total": serializers.IntegerField(),
                "sent": serializers.IntegerField(),
                "failed": serializers.IntegerField(),
                "pending": serializers.IntegerField(),
                "delivery_rate": serializers.CharField(),
                "by_channel": serializers.DictField(),
            },
        )
    },
    tags=["notifications"],
)

bulk_send_notifications_schema = extend_schema(
    summary="Bulk send notifications",
    description="Send a notification to multiple users at once. Admin only.",
    request=BulkSendNotificationSerializer,
    responses={200: NotificationSerializer(many=True)},
    tags=["notifications"],
)
