from unittest.mock import Mock

import pytest
from django.contrib.auth.models import AbstractUser

from ..models import CustomUser


class TestCustomUser:
    def test_custom_user_inherits_from_abstract(self):
        assert issubclass(CustomUser, AbstractUser)
