from django.urls import path
from .views import TemplatesListAPIView, TemplatesDetailAPIView

urlpatterns = [
    path("", TemplatesListAPIView.as_view(), name="template_list"),
    path("<int:template_id>/", TemplatesDetailAPIView.as_view(), name="template_detail"),
]
