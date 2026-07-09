from apps.ntemplates.repositories import TemplatesRepository
from apps.ntemplates.services import TemplatesService


def get_templates_repostory() -> TemplatesRepository:
    return TemplatesRepository()


def get_templates_service() -> TemplatesService:
    return TemplatesService(repo=get_templates_repostory())
