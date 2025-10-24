# syntax = docker/dockerfile:1.2
FROM python:{{ cookiecutter._python_version_specs[cookiecutter.python_version]['versions'][0] }}-slim as backend-base

ENV PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1
WORKDIR /app

ADD requirements/base.txt .

FROM backend-base as backend-dev
ADD requirements/dev.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install setuptools && pip install -r dev.txt
ADD . ./

FROM backend-base as production
ADD requirements/prod.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install setuptools && pip install -r prod.txt
ADD . ./
RUN python manage.py collectstatic --noinput
