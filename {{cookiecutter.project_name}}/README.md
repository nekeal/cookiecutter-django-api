# {{cookiecutter.full_project_name}}

[![CI](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}/actions/workflows/backend.yml/badge.svg)](https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.github_repository_name}}/actions)

{{cookiecutter.description}}

# Prerequisites

## Native way with virtualenv
- [Python3.8](https://www.python.org/downloads/)
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Docker way
- [Docker](https://docs.docker.com/engine/install/)  
- [Docker Compose](https://docs.docker.com/compose/install/)  

## Local Development

## Native way with virtualenv

First create postgresql database:

```sql
create user {{ cookiecutter.project_name }} with createdb;
alter user {{ cookiecutter.project_name }} password '{{ cookiecutter.project_name }}';
create database {{ cookiecutter.project_name }} owner {{ cookiecutter.project_name }};
```
Now you can setup virtualenv and django:
```bash
virtualenv venv
source venv/bin/activate
pip install pip-tools
make bootstrap
```

## Docker way

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```
