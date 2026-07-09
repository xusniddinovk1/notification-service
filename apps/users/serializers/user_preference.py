from typing import ClassVar

from rest_framework import serializers

from apps.users.models import Preference


class UserPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preference
        fields: ClassVar[list[str]] = [
            "id",
            "user",
            "channel",
            "is_enabled"
        ]
        read_only_fields: ClassVar[list[str]] = ["id", "user"]
