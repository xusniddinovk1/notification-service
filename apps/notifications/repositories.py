from typing import Optional, Any, TYPE_CHECKING

from django.db.models import QuerySet, Count, Q

from .models import Notification
from ..ntemplates.models import NotificationTemplate

if TYPE_CHECKING:
    from apps.users.models.users import User


class NotificationRepository:
    def get_all_notifications(self) -> QuerySet[Notification]:
        return Notification.objects.all()

    def get_user_notifications(self, user: "User") -> QuerySet[Notification]:
        return Notification.objects.filter(user=user)

    def get_notification(self, notification_id: int) -> Optional[Notification]:
        return Notification.objects.filter(id=notification_id).first()

    def get_template_by_id(self, template_id: int) -> Optional[NotificationTemplate]:
        return NotificationTemplate.objects.filter(id=template_id).first()

    def get_stats(self) -> tuple[dict[str, Any], QuerySet[Any]]:
        stats = Notification.objects.aggregate(
            total=Count("id"),
            sent=Count("id", filter=Q(status="SENT")),
            failed=Count("id", filter=Q(status="FAILED")),
            pending=Count("id", filter=Q(status="PENDING")),
        )
        by_channel = Notification.objects.values("template__channel__channel").annotate(
            count=Count("id")
        )
        return stats, by_channel

    def create_notification(self, notification: Notification) -> Notification:
        notification.save()
        return notification

    def update_notification(self, notification: Notification) -> Notification:
        notification.save()
        return notification

    def delete_notification(self, notification_id: int) -> None:
        Notification.objects.filter(id=notification_id).delete()
