from django.contrib import admin
from django.urls import include, path
{%- if cookiecutter.use_react_frontend == 'y' %}
from django.views.generic import TemplateView
{%- endif %}
{%- if cookiecutter.use_drf == "y" %}
from rest_framework.routers import DefaultRouter
{%- endif %}

{% if cookiecutter.use_drf == "y" -%}
router = DefaultRouter()
{%- endif %}

urlpatterns = [
    path("admin/", admin.site.urls),
{%- if cookiecutter.use_drf == "y" %}
    path("api/", include(router.urls)),
{%- endif %}
{%- if cookiecutter.use_react_frontend == 'y' %}
    path("", TemplateView.as_view(template_name="index.html")),
{%- endif %}
]
