"""Tests for docs/scripts/generate_cookiecutter_cli helpers."""

import pathlib
import sys

import pytest

_DOCS_SCRIPTS = pathlib.Path(__file__).resolve().parents[1] / "docs" / "scripts"
sys.path.insert(0, str(_DOCS_SCRIPTS))

from generate_cookiecutter_cli import repo_name_from_project_name  # noqa: E402


@pytest.mark.parametrize(
    ("project_name", "expected_repo_name"),
    [
        ("A Project Name", "a_project_name"),
        ("same_name_as_project", "same_name_as_project"),
        ("Test-Project Name", "test_project_name"),
    ],
)
def test_repo_name_from_project_name_matches_cookiecutter_default(
    project_name: str,
    expected_repo_name: str,
) -> None:
    """Mirrors ``repo_name`` in cookiecutter.json (slug from ``project_name``)."""
    assert repo_name_from_project_name(project_name) == expected_repo_name