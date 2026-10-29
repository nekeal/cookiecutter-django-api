validate:
    rm -rf django_app
    uv run cookiecutter --config-file tests/context.yml --no-input .
    cd django_app && git init . && git add . && uv sync && uv run pre-commit run --all-files && uv run pytest
