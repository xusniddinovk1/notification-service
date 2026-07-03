from django.urls import path
from apps.users.views import RegisterView
from apps.users.views.login import LoginView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="user-register"),
    path("login/", LoginView.as_view(), name="user-login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]
