from django.urls import path
from apps.users.views import RegisterView
from apps.users.views.login import LoginView, TokenView
from apps.users.views.user_preference import (
    UserPreferenceListView,
    UserPreferenceDetailView
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="user-register"),
    path("login/", LoginView.as_view(), name="user-login"),
    path("token/refresh/", TokenView.as_view(), name="token-refresh"),

    path("user-preferences/",
         UserPreferenceListView.as_view(), name="preference-list"),
    path("user-preferences/<int:preference_id>/",
         UserPreferenceDetailView.as_view(), name="preference-detail"),
]
