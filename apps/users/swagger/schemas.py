from ..serializers.register import RegisterSerializer
from ..serializers.user_preference import UserPreferenceSerializer
from drf_spectacular.utils import extend_schema

register_user_schema = extend_schema(
    summary="Register user",
    description="Register user",
    request=RegisterSerializer,
    responses={201: RegisterSerializer()},
    tags=["authentication"],
)

login_user_schema = extend_schema(
    summary="Login user",
    description="Login user",
    tags=["authentication"],
)

refresh_token_schema = extend_schema(
    summary="Refresh token",
    description="Refresh access token using refresh token",
    tags=["authentication"],
)
list_user_preferences_schema = extend_schema(
    summary="User preference",
    description="User preference",
    responses={200: UserPreferenceSerializer(many=True)},
    tags=["user-preferences"],
)

get_user_preference_schema = extend_schema(
    summary="Get user preference",
    description="Get user preference data by user_id",
    responses={200: UserPreferenceSerializer()},
    tags=["user-preferences"],
)

create_user_preference_schema = extend_schema(
    summary="Create user preference",
    description="Create user preference",
    request=UserPreferenceSerializer,
    responses={201: UserPreferenceSerializer()},
    tags=["user-preferences"],
)

update_user_preference_schema = extend_schema(
    summary="Update user preference",
    description="Update user preference data by user_id",
    request=UserPreferenceSerializer,
    responses={200: UserPreferenceSerializer()},
    tags=["user-preferences"],
)

delete_user_preference_schema = extend_schema(
    summary="Delete user preference",
    description="Delete user preference by user_id",
    responses={204: None},
    tags=["user-preferences"],
)
