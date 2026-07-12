import pytest
from django.contrib.auth import get_user_model

from apps.users.repositories.register import UserRepository

User = get_user_model()


@pytest.mark.django_db
def test_get_by_email_found():
    User.objects.create_user(email="test@gmail.com", password="1234string")
    repo = UserRepository()

    user = repo.get_by_email("test@gmail.com")
    assert user is not None
    assert user.email == "test@gmail.com"


@pytest.mark.django_db
def test_get_by_email_not_found():
    repo = UserRepository()

    user = repo.get_by_email("test1@gmail.com")

    assert user is None
