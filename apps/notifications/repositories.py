from django.db.models import QuerySet

from .models import Notification, notification
from ..ntemplates.models import NotificationTemplate


class NotificationRepository:
    def get_all_notifications(self) -> QuerySet[Notification]:
        return Notification.objects.all()

    def get_user_notifications(self, user) -> QuerySet[Notification]:
        return Notification.objects.filter(user=user)

    def get_notification(self, notification_id: int) -> Notification:
        return Notification.objects.filter(id=notification_id).first()

    def get_template_by_id(self, template_id: int) -> NotificationTemplate:
        return NotificationTemplate.objects.filter(id=template_id).first()

    def create_notification(self, notification: Notification) -> Notification:
        notification.save()
        return notification

    def update_notification(self, notification: Notification) -> Notification:
        notification.save()
        return notification

    def delete_notification(self, notification_id: int) -> None:
        Notification.objects.filter(id=notification_id).delete()
