from typing import Optional, Any, TYPE_CHECKING
from django.db.models import QuerySet
from django.http import Http404
from rest_framework.exceptions import ValidationError

from .tasks import send_notification_task
from .models import Notification
from .repositories import NotificationRepository
from ..users.repositories.user_preferences import UserPreferenceRepository

if TYPE_CHECKING:
    from apps.users.models.users import User


class NotificationService:
    def __init__(
        self, repo: NotificationRepository, preference_repo: UserPreferenceRepository
    ) -> None:
        self.repo = repo
        self.preference_repo = preference_repo

    def get_notifications(self) -> QuerySet[Notification]:
        return self.repo.get_all_notifications()

    def list_notifications(self, user: "User") -> QuerySet[Notification]:
        if user.is_staff:
            return self.repo.get_all_notifications()
        return self.repo.get_user_notifications(user=user)

    def get_notification(self, user: "User", notification_id: int) -> Notification:
        notification = self.repo.get_notification(notification_id)
        if not notification:
            raise Http404(f"Notification with id {notification_id} not found")
        if not user.is_staff and notification.user != user:
            raise Http404("Not found")
        return notification

    def create_notification(
        self, user_id: int, template_id: int, payload: dict
    ) -> Notification:
        user = self.repo.get_user_by_id(user_id)
        if not user:
            raise Http404(f"User with id {user_id} not found")

        template = self.repo.get_template_by_id(template_id)
        if not template:
            raise Http404(f"Template with id {template_id} not found")

        channel = template.channel
        preference = self.preference_repo.get_preference_by_user_and_channel(
            user, channel
        )
        if preference and not preference.is_enabled:
            raise ValidationError("User has disabled this notification channel")

        notification = Notification(
            user=user,
            template=template,
            payload=payload,
            status=Notification.STATUS.PENDING,
        )
        self.repo.create_notification(notification)
        send_notification_task.delay(notification.id)

        return notification

    def update_status(
        self, user: "User", notification_id: int, status: str
    ) -> Optional[Notification]:
        notification = self.get_notification(user=user, notification_id=notification_id)

        if notification is None:
            return None

        notification.status = status
        self.repo.update_notification(notification)
        return notification

    def get_stats(self) -> dict[str, Any]:
        stats, by_channel = self.repo.get_stats()

        total = stats["total"]
        sent = stats["sent"]
        delivery_rate = f"{(sent / total * 100):.1f}%" if total > 0 else "0%"

        channel_stats = {
            item["template__channel__channel"]: item["count"] for item in by_channel
        }

        return {
            **stats,
            "delivery_rate": delivery_rate,
            "by_channel": channel_stats,
        }
