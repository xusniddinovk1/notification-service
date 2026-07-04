from apps.users.repositories.user_preferences import UserPreferenceRepository
from apps.users.services.user_preference import UserPreferenceService


def get_preference_repository() -> UserPreferenceRepository:
    return UserPreferenceRepository()


def get_preference_service() -> UserPreferenceService:
    return UserPreferenceService(
        repo=get_preference_repository(),
    )
