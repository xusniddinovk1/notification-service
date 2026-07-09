from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from ..models.user_preference import Preference
from ..container import get_preference_service
from ..serializers.user_preference import UserPreferenceSerializer
from ..services.user_preference import UserPreferenceService
from ..swagger.schemas import (
    list_user_preferences_schema,
    get_user_preference_schema,
    create_user_preference_schema,
    update_user_preference_schema,
    delete_user_preference_schema
)


class UserPreferenceListView(APIView):
    permission_classes = [IsAuthenticated]
    service: UserPreferenceService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_preference_service()

    @list_user_preferences_schema
    def get(self, request: Request) -> Response:
        user_preferences = self.service.list_preferences(request.user)
        serializer = UserPreferenceSerializer(user_preferences, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @create_user_preference_schema
    def post(self, request: Request) -> Response:
        serializer = UserPreferenceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        preference = Preference(user=request.user, **serializer.validated_data)
        created_preference = self.service.create_preference(preference)
        return Response(
            UserPreferenceSerializer(created_preference).data,
            status=HTTP_201_CREATED
        )


class UserPreferenceDetailView(APIView):
    permission_classes = [IsAuthenticated]
    service: UserPreferenceService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_preference_service()

    @get_user_preference_schema
    def get(self, request: Request, preference_id: int) -> Response:
        user_preference = self.service.get_user_preference(request.user, preference_id)
        serializer = UserPreferenceSerializer(user_preference)
        return Response(serializer.data, status=HTTP_200_OK)

    @update_user_preference_schema
    def put(self, request: Request, preference_id: int) -> Response:
        serializer = UserPreferenceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        preference = self.service.get_user_preference(request.user, preference_id)
        preference.channel = serializer.validated_data['channel']
        preference.is_enabled = serializer.validated_data['is_enabled']
        updated_preference = self.service.update_preference(request.user, preference_id, preference)
        return Response(
            UserPreferenceSerializer(updated_preference).data,
            status=HTTP_200_OK
        )

    @delete_user_preference_schema
    def delete(self, request: Request, preference_id: int) -> Response:
        self.service.delete_preference(request.user, preference_id)
        return Response(status=HTTP_204_NO_CONTENT)
