from django.contrib.auth.models import AbstractUser

from {{ cookiecutter.project_name }}.accounts.models import CustomUser
from {{ cookiecutter.project_name }}.accounts.factories import UserFactory


class TestCustomUser:
    def test_custom_user_inherits_from_abstract(self):
        assert issubclass(CustomUser, AbstractUser)

    def test_factory_builds_user(self):
        user = UserFactory.build(password="password")  # noqa: S106
        assert user.password != "password"
