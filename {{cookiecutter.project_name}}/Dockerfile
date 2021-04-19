# syntax = docker/dockerfile:1.2
{%- if cookiecutter.use_react_frontend == 'y' %}
FROM node:14.16.1-slim as frontend-dev
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
ENV YARN_CACHE_FOLDER /tmp/.yarn
ENV CYPRESS_SKIP_BINARY_INSTALL 1

COPY ["{{ cookiecutter.project_name }}/frontend/package.json",\
      "{{ cookiecutter.project_name }}/frontend/yarn.lock",\
      "./"\
     ]
RUN --mount=type=cache,target=/tmp/.yarn yarn install
COPY {{ cookiecutter.project_name }}/frontend .
CMD yarn start

FROM frontend-dev as frontend-builder
WORKDIR /app
COPY --from=frontend-dev /app ./
RUN yarn build

FROM alpine as frontend-build
WORKDIR /app
COPY --from=frontend-builder /app/build ./build
COPY --from=frontend-builder /app/webpack-stats.json ./
{%- endif %}

FROM python:3.8.7-slim as backend-base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

ADD requirements/base.txt .

FROM backend-base as backend-dev
ADD requirements/dev.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install -r dev.txt
ADD . ./

FROM backend-base as production
ADD requirements/prod.txt .
RUN --mount=type=cache,target=/root/.cache/pip pip install -r prod.txt
ADD . ./
{%- if cookiecutter.use_react_frontend == 'y' %}
COPY --from=frontend-build /app/build ./{{ cookiecutter.project_name }}/frontend/build
COPY --from=frontend-build /app/webpack-stats.json ./{{ cookiecutter.project_name }}/frontend/
{%- endif %}
RUN python manage.py collectstatic --noinput
