from django.contrib import admin
from django.urls import include, path
{%- if cookiecutter.use_react_frontend == 'y' %}
from django.views.generic import TemplateView
{%- endif %}
{%- if cookiecutter.use_drf_yasg == "y" %}
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
{%- endif %}
{%- if cookiecutter.use_drf == "y" %}
from rest_framework.routers import DefaultRouter
{%- endif %}

{% if cookiecutter.use_drf_yasg == "y" -%}
schema_view = get_schema_view(
    openapi.Info(
        title="{{ cookiecutter.full_project_name }} API",
        default_version="v1",
        contact=openapi.Contact(email="{{ cookiecutter.email }}"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
{%- endif %}

{% if cookiecutter.use_drf == "y" -%}
router = DefaultRouter()
{%- endif %}

urlpatterns = [
    path("admin/", admin.site.urls),
{%- if cookiecutter.use_drf == "y" %}
    path("api/", include(router.urls)),
{%- endif %}
{%- if cookiecutter.use_drf_yasg == "y" %}
    path('api/doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger'),
{%- endif %}
{%- if cookiecutter.use_react_frontend == 'y' %}
    path("", TemplateView.as_view(template_name="index.html")),
{%- endif %}
{%- if cookiecutter.use_django_debug_toolbar == 'y' %}
    path("__debug__/", include("debug_toolbar.urls")),
{%- endif %}
]
