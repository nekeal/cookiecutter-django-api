from django.urls import include, path

app_name = "accounts"

urlpatterns = [
{%- if cookiecutter.use_jwt == "y" %}
    path(r"", include("djoser.urls")),
{%- endif %}
]
