import dataclasses
import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from cookiecutter.main import cookiecutter

TEMPLATE_DIR = Path(__file__).parent.parent


@dataclasses.dataclass
class CookiecutterProjectGenerator:
    template_dir: Path
    output_dir: Path
    default_context: dict[str, str] = dataclasses.field(default_factory=dict)

    def generate_project(self, extra_context: dict[str, str] | None = None) -> Path:
        """Generate a project using the template from the specified directory and return the path to the generated directory"""
        context = self.default_context | (extra_context or {})
        cookiecutter(
            str(self.template_dir),
            output_dir=str(self.output_dir),
            no_input=True,
            extra_context=context,
        )
        return self.output_dir / context["project_name"]


@pytest.fixture
def cookie_generator(tmp_path, context):
    return CookiecutterProjectGenerator(TEMPLATE_DIR, tmp_path, default_context=context)


@pytest.fixture
def context():
    return yaml.load(
        (Path(__file__).parent / "context.yml").read_text(), Loader=yaml.SafeLoader
    )["default_context"]


def test_default_project_generation(cookie_generator):
    project_dir = cookie_generator.generate_project()

    assert project_dir.exists()
    assert (project_dir / "pyproject.toml").exists()


def test_newly_generated_project_can_resolve_and_install_requirements(cookie_generator):
    """
    This tests validates whether there is no mistake in the generated requirements.
    Also, it creates virtualenv and installs the requirements.
    """
    project_dir = cookie_generator.generate_project()

    subprocess.run(
        ["uv", "sync"],
        timeout=20,
        stdout=sys.stdout,
        stderr=sys.stderr,
        check=True,
        cwd=project_dir,
    )

    assert (project_dir / ".venv").exists()
    assert (project_dir / "uv.lock").exists()
