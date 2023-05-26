import os
import sys
# TODO:
REMOVE_PATHS = [
    '{%- if cookiecutter.use_drf != "y" %} accounts/serializers.py {% endif %}',
    '{%- if cookiecutter.use_celery != "y" %} celery.py {% endif %}',
    '{%- if cookiecutter.use_react_frontend != "y" %} index.html {% endif %}',
]

for path in REMOVE_PATHS:
    path = path.strip()
    if path and os.path.exists(path):
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.unlink(path)