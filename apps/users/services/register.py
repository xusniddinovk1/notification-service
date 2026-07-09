
from apps.users.models import User
from apps.users.repositories.register import UserRepository
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegisterService:
    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def register(
            self,
            email: str,
            password: str,
            **extra_fields: str
    ) -> tuple[User, dict[str, str]]:
        user = self.repo.create(email=email, password=password, **extra_fields)
        tokens = self._generate_tokens(user)
        return user, tokens

    def _generate_tokens(self, user: User) -> dict[str, str]:
        refresh = RefreshToken.for_user(user)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }
