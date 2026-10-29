# AGENTS.md

## Project overview

Cookiecutter template for generating Django API projects. The template source is in `{{cookiecutter.project_name}}/`; `django_app/` is generated output and should not be edited by hand.

## Key files

- `cookiecutter.json` — prompt variables and options.
- `hooks/post_gen_project.py` — removes optional files after generation.
- `{{cookiecutter.project_name}}/` — the actual project template.
- `tests/` and `tests/context.yml` — tests for project generation.

## Commands

```bash
uv sync          # install tooling
uv run pytest    # run generation tests
just validate    # regenerate django_app/ and run pre-commit + pytest inside it
```

## Conventions

- Use `uv`, not `pip`.
- Python 3.12+; Ruff for linting/formatting; pytest for tests.
- Keep Jinja tags (`{{ cookiecutter.* }}`) valid.
- Do not edit `django_app/` directly; regenerate it.
