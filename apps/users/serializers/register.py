from rest_framework import serializers
from apps.users.models import User
from apps.users.services.register import UserRegisterService
from apps.users.repositories.register import (
    UserRepository,
)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ["email", "password", "first_name", "last_name"]

    def create(self, validated_data):
        service = UserRegisterService(repo=UserRepository())
        return service.register(**validated_data)
