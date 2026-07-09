from typing import Optional

from django.db.models import QuerySet

from apps.nchannels.models import NotificationChannel


class NotificationChannelRepository:
    def get_all_channel(self) -> QuerySet[NotificationChannel]:
        return NotificationChannel.objects.all()

    def get_channel_by_id(self, channel_id: int) -> Optional[NotificationChannel]:
        return NotificationChannel.objects.filter(id=channel_id).first()

    def create_channel(self, entity: NotificationChannel) -> NotificationChannel:
        entity.save()
        return entity

    def update_channel(self, entity: NotificationChannel) -> NotificationChannel:
        entity.save()
        return entity

    def delete_channel(self, entity_id: int) -> None:
        NotificationChannel.objects.filter(id=entity_id).delete()
