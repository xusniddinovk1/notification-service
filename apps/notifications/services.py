from django.db.models import QuerySet
from django.http import Http404
from .tasks import send_notification_task
from .models import Notification
from .repositories import NotificationRepository


class NotificationService:
    def __init__(self, repo: NotificationRepository):
        self.repo = repo

    def get_notifications(self):
        return self.repo.get_all_notifications()

    def list_notifications(self, user) -> QuerySet[Notification]:
        return self.repo.get_user_notifications(user=user)

    def get_notification(self, notification_id: int) -> Notification:
        notification = self.repo.get_notification(notification_id)
        if not notification:
            raise Http404(f"Notification with id {notification_id} not found")
        return notification

    def create_notification(self, user, template_id: int, payload: dict) -> Notification:
        template = self.repo.get_template_by_id(template_id)
        if not template:
            raise Http404(f"Template with id {template_id} not found")
        notification = Notification(
            user=user,
            template=template,
            payload=payload,
            status=Notification.STATUS.PENDING
        )
        self.repo.create_notification(notification)
        send_notification_task.delay(notification.id)

        return notification

    def update_status(self, notification_id: int, status: str) -> Notification:
        notification = self.get_notification(notification_id)
        notification.status = status
        self.repo.update_notification(notification)
        return notification
