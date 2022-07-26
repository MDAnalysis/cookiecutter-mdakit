import pytest
from cookiecutter.main import cookiecutter

from .utils import CookiecutterMDAKit


class TestAnalysis:

    @pytest.mark.parametrize("analysis_name", ["", "Enter"])
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

            assert kit.cookie_package_path_exists("analysis/myanalysisclass.py")
            assert kit.cookie_package_path_exists("tests/analysis/test_myanalysisclass.py")
            assert "MyAnalysisClass" in kit.get_classes_from_package_file("analysis/myanalysisclass.py")
            assert "TestMyAnalysisClass" in kit.get_classes_from_package_file("tests/analysis/myanalysisclass.py")
