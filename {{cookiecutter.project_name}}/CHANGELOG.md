# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-10-31

### Added
- Switched to `uv` for dependency management.
- All dependencies are now managed in `pyproject.toml`.
- `django-extensions` is now a default dependency.
- Added more `ruff` checks for better code quality.
- Added initial user fixture.

### Changed
- Updated `Makefile` and `Dockerfile` to use `uv`.
- Updated `pre-commit-config.yaml` to use `uv run`.
- Updated `README.md` with the new dependency management tool.

### Removed
- Removed React frontend support.
- Removed JWT authentication with `djoser`.

## [Unreleased]
