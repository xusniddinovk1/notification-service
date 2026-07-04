from apps.users.models import Preference


class UserPreferenceRepository:
    def get_channel_preferences(self, user):
        return Preference.objects.filter(user=user)

    def get_channel_preference(self, preference_id: int):
        return Preference.objects.filter(id=preference_id).first()

    def create_preference(self, entity: Preference) -> Preference:
        entity.save()
        return entity

    def update_preference(self, preference: Preference) -> Preference:
        preference.save()
        return preference

    def delete_preference(self, preference_id: int):
        Preference.objects.filter(id=preference_id).delete()
