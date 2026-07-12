from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from ..swagger.schemas import login_user_schema, refresh_token_schema
from ..throttles import LoginRateThrottle


@login_user_schema
class LoginView(TokenObtainPairView):
    throttle_classes = [LoginRateThrottle]

    pass


@refresh_token_schema
class TokenView(TokenRefreshView):
    pass
