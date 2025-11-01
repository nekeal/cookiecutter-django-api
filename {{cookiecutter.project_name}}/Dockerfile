# syntax = docker/dockerfile:1.2
FROM python:{{ cookiecutter._python_version_specs[cookiecutter.python_version]['versions'][0] }}-slim as backend-base

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1
WORKDIR /app

# Install uv package manager
RUN pip install --upgrade pip uv

FROM backend-base as backend-dev
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/ uv sync --group dev
ADD . ./

FROM backend-base as production
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv uv sync --no-dev --group prod
ADD . ./
RUN python manage.py collectstatic --noinput
