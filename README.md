# Cookiecutter Django API

This template will help you create Django API with most tools you need to create 
quality web app.

## Highlights
- Django 4.0+
- Python 3.10+
- Pip Tool for dependency management
- Testing with pytest
- Isolated tests with tox
- Autoformatting with black & isort
- Linting with flake8
- Type checking with mypy
- Support for frontend using webpack
- Multistage Dockerfile with optional building frontend.
- Local docker-compose

## Quick Start

Install [cookiecutter](https://github.com/audreyr/cookiecutter):

For debian base distribution
```bash
apt install cookiecutter
```

For MacOS
```bash
brew install cookiecutter
```

Create your project:
```
cookiecutter gh:nekeal/cookiecutter-django-api
```

Example of the result: [django-template-project](https://github.com/nekeal/django-template-project)
