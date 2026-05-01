import pathlib

import pytest

from .utils import (
    DEFAULT_LICENSE,
    CookiecutterMDAKit,
    LICENSE_SOURCE_FILENAMES,
)

LICENSES = [
    ("MIT License", "MIT License", True),
    (
        "GNU General Public License v3 or later (GPL-3.0+)",
        "GNU GENERAL PUBLIC LICENSE",
        True,
    ),
    ("BSD 3-Clause License", "BSD 3-Clause License", True),
    ("Apache License 2.0", "Apache License", True),
]


@pytest.mark.parametrize(
    ("license_option", "expected_substring", "expect_license_file"),
    LICENSES,
)
def test_license_matrix(tmpdir, license_option, expected_substring, expect_license_file):
    repo_name = "mdakit-test"
    with tmpdir.as_cwd():
        kit = CookiecutterMDAKit(
            repo_name=repo_name,
            package_name="lic_test_pkg",
            license=license_option,
            output_directory=".",
            template_analysis_class="",
        )
        kit.run()
    root = pathlib.Path(str(tmpdir)) / repo_name
    licenses_root = root / "licenses"
    for name in LICENSE_SOURCE_FILENAMES:
        assert not (licenses_root / name).exists()
    assert not licenses_root.exists()

    license_path = root / "LICENSE"
    if expect_license_file:
        assert license_path.is_file()
        body = license_path.read_text(encoding="utf-8")
        assert expected_substring in body
        if license_option.startswith("GNU General Public License v3"):
            assert "Version 3," in body
    else:
        assert not license_path.exists()


def test_dataclass_default_license():
    """Test default license to MIT"""
    assert CookiecutterMDAKit().license == DEFAULT_LICENSE
    assert CookiecutterMDAKit().license == LICENSES[0][0]
