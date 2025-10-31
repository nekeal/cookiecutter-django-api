# Cookiecutter Django API

[![CI](https://github.com/nekeal/cookiecutter-django-api/actions/workflows/test-template.yml/badge.svg)](https://github.com/nekeal/cookiecutter-django-api/actions/workflows/test-template.yml)

A modern, production-ready cookiecutter template for creating Django APIs.

This template provides a solid foundation for building robust and scalable Django applications with a focus on best practices and developer experience.

## Features

-   **Modern Python:** Python 3.12+
-   **Latest Django:** Django 5.2+
-   **Dependency Management:** `uv` for fast and reliable dependency management.
-   **Code Quality:**
    -   `ruff` for linting and auto-formatting.
    -   `mypy` for static type checking.
-   **Testing:**
    -   `pytest` for writing and running tests.
    -   `tox` for testing against multiple Python versions.
-   **Containerization:**
    -   `Dockerfile` for building production-ready Docker images.
    -   `docker-compose.yml` for local development.

## Getting Started

### Prerequisites

-   [Python 3.12+](https://www.python.org/downloads/)
-   [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html)

### Installation

To create a new project, run:

```bash
cookiecutter gh:nekeal/cookiecutter-django-api
```

This will prompt you for some basic information about your project, and then generate a new Django project for you.

## Usage

After generating your project, you can start the local development server with:

```bash
make bootstrap
make run
```

This will start the Django development server at `http://localhost:8000`.

## Contributing

Contributions are welcome!

## License

This project is licensed under the terms of the [MIT license](LICENSE).