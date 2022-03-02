{%- if cookiecutter.use_jwt == "y" -%}
from djoser.views import UserViewSet


class CustomUserViewSet(UserViewSet):
    pass
{%- endif %}
