from rest_framework import serializers

from apps.users.models import Preference


class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields = ["id", "user", "channel", "is_enabled"]
        read_only_fields = ["id", "user"]
