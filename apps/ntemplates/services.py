from django.db.models import QuerySet
from django.http import Http404
from django.core.cache import cache
from .models import NotificationTemplate
from .repositories import TemplatesRepository


class TemplatesService:
    def __init__(
        self,
        repo: TemplatesRepository,
    ) -> None:
        self.repo = repo

    def list_templates(self) -> QuerySet[NotificationTemplate]:
        cached = cache.get("templates_list")
        if cached:
            return cached
        templates = self.repo.get_all_templates()
        cache.set("templates_list", templates, timeout=300)
        return templates

    def get_template(self, template_id: int) -> NotificationTemplate:
        template = self.repo.get_template(template_id)
        if not template:
            raise Http404(f"Template with id {template_id} not found")
        return template

    def create_template(
        self, template_data: NotificationTemplate
    ) -> NotificationTemplate:
        self.repo.create_template(template_data)
        cache.delete("templates_list")
        return template_data

    def update_template(
        self, template_id: int, template_data: NotificationTemplate
    ) -> NotificationTemplate:
        template = self.repo.get_template(template_id)
        if not template:
            raise Http404(f"Template with id {template_id} not found")
        self.repo.update_template(template_data)
        cache.delete("templates_list")
        return template_data

    def delete_template(self, template_id: int) -> None:
        template = self.repo.get_template(template_id)
        if not template:
            raise Http404(f"Template with id {template_id} not found")
        self.repo.delete_template(template_id)
        cache.delete("templates_list")
