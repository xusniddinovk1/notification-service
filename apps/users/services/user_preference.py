from django.db.models import QuerySet
from django.http import Http404

from apps.users.models import Preference
from apps.users.repositories.user_preferences import UserPreferenceRepository


class UserPreferenceService:
    def __init__(self, repo: UserPreferenceRepository) -> None:
        self.repo = repo

    def list_preferences(self, user) -> QuerySet[Preference]:
        return self.repo.get_channel_preferences(user)

    def get_user_preference(self, user, preference_id: int) -> Preference:
        preference = self.repo.get_channel_preference(preference_id)
        if not preference:
            raise Http404(f"Preference with id {preference_id} not found")
        if preference.user != user:
            raise Http404(f"Preference with user {user} not found")
        return preference

    def create_preference(self, preference: Preference) -> Preference:
        self.repo.create_preference(preference)
        return preference

    def update_preference(self, user, preference_id: int, preference_data: Preference) -> Preference:
        preference = self.get_user_preference(user, preference_id)
        if not preference:
            raise Http404(f"Preference with id {preference_id} not found")
        self.repo.update_preference(preference_data)
        return preference_data

    def delete_preference(self, user, preference_id: int) -> None:
        self.get_user_preference(user, preference_id)
        self.repo.delete_preference(preference_id)
