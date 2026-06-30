from apps.users.repositories.register import UserRepository
from apps.users.serializers.register import RegisterSerializer


class UserRegisterService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, email: str, password: str, **extra_fields):
        user = self.repo.create(email=email, password=password, **extra_fields)
        return user
