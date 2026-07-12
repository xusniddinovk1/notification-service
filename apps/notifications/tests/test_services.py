import pytest
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

from apps.nchannels.models import NotificationChannel
from apps.notifications.repositories import NotificationRepository
from apps.notifications.services import NotificationService
from apps.ntemplates.models import NotificationTemplate
from apps.users.models import Preference
from apps.users.repositories.user_preferences import UserPreferenceRepository

User = get_user_model()


@pytest.mark.django_db
def test_create_notification(mocker):
    user = User.objects.create_user(email="test@gmail.com", password="1234string")
    channel = NotificationChannel.objects.create(channel="EMAIL")
    template = NotificationTemplate.objects.create(
        title="Welcome", content="Hello {{ first_name }}", channel=channel
    )

    mock_task = mocker.patch("apps.notifications.tasks.send_notification_task.delay")

    service = NotificationService(
        repo=NotificationRepository(),
        preference_repo=UserPreferenceRepository(),
    )

    notification = service.create_notification(
        user_id=user.id, template_id=template.id, payload={"first_name": "Ali"}
    )

    assert notification.status == "PENDING"
    assert notification.user == user
    mock_task.assert_called_once_with(notification.id)


@pytest.mark.django_db
@pytest.mark.django_db
def test_create_notification_blocked_by_preference(mocker):
    user = User.objects.create_user(email="test@gmail.com", password="1234string")
    channel = NotificationChannel.objects.create(channel="EMAIL")
    template = NotificationTemplate.objects.create(
        title="Welcome", content="Hello {{ first_name }}", channel=channel
    )
    Preference.objects.create(user=user, channel=channel, is_enabled=False)

    mock_task = mocker.patch("apps.notifications.tasks.send_notification_task.delay")

    service = NotificationService(
        repo=NotificationRepository(),
        preference_repo=UserPreferenceRepository(),
    )

    with pytest.raises(ValidationError):
        service.create_notification(
            user_id=user.id, template_id=template.id, payload={"first_name": "Ali"}
        )

    mock_task.assert_not_called()
