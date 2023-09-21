import pytest
from cookiecutter.main import cookiecutter

from .utils import CookiecutterMDAKit


class TestAnalysis:

    @pytest.mark.parametrize("analysis_name", ["", "Press Enter to skip"])
    def test_no_analysis(self, tmpdir, analysis_name):
        with tmpdir.as_cwd():
            kit = CookiecutterMDAKit(template_analysis_class=analysis_name)
            kit.run()

            assert not kit.cookie_package_path_exists("analysis")
            assert not kit.cookie_package_path_exists("tests/analysis")

    def test_analysis(self, tmpdir):
        with tmpdir.as_cwd():
            kit = CookiecutterMDAKit(template_analysis_class="MyAnalysisClass")
            kit.run()

            for clsname, file in (
                ("MyAnalysisClass", "analysis/myanalysisclass.py"),
                ("TestMyAnalysisClass", "tests/analysis/test_myanalysisclass.py"),
            ):
                assert kit.cookie_package_path_exists(file)
                assert clsname in kit.get_classes_from_package_file(file)


class TestGitHubHostAccount:
    def test_official_mda_theme(self, tmpdir):
        with tmpdir.as_cwd():
            kit = CookiecutterMDAKit(github_host_account="MDAnalysis")
            kit.run()

            conf = kit.cookie_directory / "docs/source/conf.py"
            assert conf.is_file()

            text = conf.read_text()
            assert '"mda_official": True,' in text
            assert "html_logo" not in text
            assert "html_favicon" not in text

    def test_non_official_mda_theme(self, tmpdir):
        with tmpdir.as_cwd():
            kit = CookiecutterMDAKit(github_host_account="other")
            kit.run()

            conf = kit.cookie_directory / "docs/source/conf.py"
            assert conf.is_file()

            text = conf.read_text()
            patterns = [
                '"mda_official": False,',
                'html_logo = "_static/logo/placeholder_logo.png"',
                'html_favicon = "_static/logo/placeholder_favicon.svg"',
            ]
            for pattern in patterns:
                assert pattern in text, f"{pattern} not found"
