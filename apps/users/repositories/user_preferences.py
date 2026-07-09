from typing import Optional

from django.db.models import QuerySet

from apps.nchannels.models import NotificationChannel
from apps.users.models import Preference
from django.contrib.auth import get_user_model

User = get_user_model()


class UserPreferenceRepository:
    def get_channel_preferences(self, user: User) -> QuerySet[Preference]:
        return Preference.objects.filter(user=user)

    def get_channel_preference(self, preference_id: int) -> Optional[Preference]:
        return Preference.objects.filter(id=preference_id).first()

    def get_preference_by_user_and_channel(
            self,
            user: User,
            channel: NotificationChannel
    ) -> Preference:
        return Preference.objects.filter(
            user=user,
            channel=channel
        ).first()

    def create_preference(
            self,
            entity: Preference
    ) -> Preference:
        entity.save()
        return entity

    def update_preference(
            self,
            preference: Preference
    ) -> Preference:
        preference.save()
        return preference

    def delete_preference(self, preference_id: int) -> None:
        Preference.objects.filter(id=preference_id).delete()
