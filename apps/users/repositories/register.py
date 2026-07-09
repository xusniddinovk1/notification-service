from typing import Optional, TYPE_CHECKING, cast

from apps.users.models import User

if TYPE_CHECKING:
    from apps.users.models import User


class UserRepository:
    def create(self, email: str, password: str, **extra_fields: str) -> User:
        user = User.objects.create_user(email=email, password=password, **extra_fields)
        return cast(User, user)

    def get_by_email(self, email: str) -> Optional[User]:
        return User.objects.filter(email=email).first()
