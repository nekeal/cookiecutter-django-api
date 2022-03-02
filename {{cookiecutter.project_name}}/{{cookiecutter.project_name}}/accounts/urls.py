from django.urls import include, path

app_name = "accounts"

urlpatterns = [
{%- if cookiecutter.use_jwt == "y" %}
    path(r"", include("djoser.urls")),
    path(r"", include("djoser.urls.jwt")),
    {%- endif %}
]
