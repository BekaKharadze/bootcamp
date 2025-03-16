from django.urls import path, re_path
from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Product API",
        default_version='v1',
        description="API documentation for Product CRUD",
    ),
    public=True,
)

urlpatterns = [
    re_path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]