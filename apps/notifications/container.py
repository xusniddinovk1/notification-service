from apps.notifications.repositories import NotificationRepository
from apps.notifications.services import NotificationService
from apps.users.repositories.user_preferences import UserPreferenceRepository


def get_notification_repository() -> NotificationRepository:
    return NotificationRepository()


def get_notification_service() -> NotificationService:
    return NotificationService(
        repo=get_notification_repository(),
        preference_repo=UserPreferenceRepository(),
    )
