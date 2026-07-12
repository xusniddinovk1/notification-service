import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(email="test@gmail.com", password="1234string")

    result = user.check_password("1234string")

    assert result is True


@pytest.mark.django_db
def test_create_superuser():
    user = User.objects.create_superuser(email="test@gmail.com", password="1234admin")

    result = user.check_password("1234admin")
    assert user.is_staff is True
    assert user.is_superuser is True
    assert result is True
