from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from .models import NotificationTemplate
from .serializers import TemplatesSerializer
from .container import get_templates_service
from .services import TemplatesService
from .swagger.schemas import (
    list_templates_schema,
    get_template_by_id_schema,
    create_template_schema,
    update_template_by_id_schema,
    delete_template_by_id_schema
)


class TemplatesListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    service: TemplatesService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_templates_service()

    @list_templates_schema
    def get(self, request: Request) -> Response:
        templates_list = self.service.list_templates()
        serializer = TemplatesSerializer(templates_list, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    @create_template_schema
    def post(self, request: Request) -> Response:
        serializer = TemplatesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        template = NotificationTemplate(**serializer.validated_data)
        created_data = self.service.create_template(template)
        return Response(
            TemplatesSerializer(created_data).data,
            status=HTTP_201_CREATED,
        )


class TemplatesDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]
    service: TemplatesService

    def __init__(self, **kwargs: object) -> None:
        super().__init__(**kwargs)
        self.service = get_templates_service()

    @get_template_by_id_schema
    def get(self, request: Request, template_id: int) -> Response:
        template = self.service.get_template(template_id)
        serializer = TemplatesSerializer(template)
        return Response(serializer.data, status=HTTP_200_OK)

    @update_template_by_id_schema
    def put(self, request: Request, template_id: int) -> Response:
        serializer = TemplatesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        template = self.service.get_template(template_id)
        template.title = serializer.validated_data.get('title', template.title)
        template.subject = serializer.validated_data.get('subject', template.subject)
        template.content = serializer.validated_data.get('content', template.content)
        template.channel = serializer.validated_data.get('channel', template.channel)
        template.is_active = serializer.validated_data.get('is_active', template.is_active)
        updated_template = self.service.update_template(template_id, template)
        return Response(
            TemplatesSerializer(updated_template).data,
            status=HTTP_200_OK,
        )

    @delete_template_by_id_schema
    def delete(self, request: Request, template_id: int) -> Response:
        self.service.delete_template(template_id)
        return Response(status=HTTP_204_NO_CONTENT)
