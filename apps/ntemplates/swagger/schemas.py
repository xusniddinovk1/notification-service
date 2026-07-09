from ..serializers import TemplatesSerializer
from drf_spectacular.utils import extend_schema

list_templates_schema = extend_schema(
    summary="List of notification templates",
    description="List of notification templates",
    responses={200: TemplatesSerializer(many=True)},
    tags=["templates"]
)

get_template_by_id_schema = extend_schema(
    summary="Get template",
    description="Get template data by id",
    responses={200: TemplatesSerializer()},
    tags=["templates"]
)

create_template_schema = extend_schema(
    summary="Create template",
    description="Create template data",
    request=TemplatesSerializer,
    responses={200: TemplatesSerializer()},
    tags=["templates"]
)

update_template_by_id_schema = extend_schema(
    summary="Update template",
    description="Update template data by id",
    request=TemplatesSerializer,
    responses={200: TemplatesSerializer()},
    tags=["templates"]
)

delete_template_by_id_schema = extend_schema(
    summary="Delete template",
    description="Delete template data",
    responses={204: None},
    tags=["templates"]
)
