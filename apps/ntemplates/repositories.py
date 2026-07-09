from typing import Optional

from django.db.models import QuerySet
from .models import NotificationTemplate


class TemplatesRepository:
    def get_all_templates(self) -> QuerySet[NotificationTemplate]:
        return NotificationTemplate.objects.all()

    def get_template(self, template_id: int) -> Optional[NotificationTemplate]:
        return NotificationTemplate.objects.filter(id=template_id).first()

    def create_template(self, entity: NotificationTemplate) -> NotificationTemplate:
        entity.save()
        return entity

    def update_template(self, entity: NotificationTemplate) -> NotificationTemplate:
        entity.save()
        return entity

    def delete_template(self, entity_id: int) -> None:
        NotificationTemplate.objects.filter(id=entity_id).delete()
