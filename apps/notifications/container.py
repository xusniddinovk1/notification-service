from apps.notifications.repositories import NotificationRepository
from apps.notifications.services import NotificationService


def get_notification_repository() -> NotificationRepository:
    return NotificationRepository()


def get_notification_service() -> NotificationService:
    return NotificationService(
        repo=get_notification_repository(),
    )
