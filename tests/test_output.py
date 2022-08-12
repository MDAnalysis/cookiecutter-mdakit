import pytest

from .utils import CookiecutterMDAKit, DependencyType


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

            clsname = "MyAnalysisClass"
            clsfile = "analysis/myanalysisclass.py"
            testcls = "TestMyAnalysisClass"
            testfile = "tests/analysis/test_myanalysisclass.py"

            assert kit.cookie_package_path_exists(clsfile)
            assert clsname in kit.get_classes_from_package_file(clsfile)
            assert kit.cookie_package_path_exists(testfile)
            assert testcls in kit.get_classes_from_package_file(testfile)


@pytest.mark.parametrize("dependency_source", DependencyType)
@pytest.mark.parametrize("include_ReadTheDocs", ["y", "n"])
def test_write_outputs(
    test_output_directory,
    dependency_source,
    include_ReadTheDocs
):
    if include_ReadTheDocs == "y":
        rtd_name = "ReadTheDocs"
    else:
        rtd_name = "no-ReadTheDocs"

    dep_name = f"{dependency_source.name.lower()}-deps"
    project_name = f"TestMDAKit_with_{dep_name}_and_{rtd_name}"
    description = (
        "Test MDAKit Project with "
        f"dependencies using {dependency_source.name.lower()} "
        f"and {rtd_name.replace('-', ' ')}"
    )

    output_directory = test_output_directory / project_name
    output_directory.mkdir(exist_ok=True)
    kitter = CookiecutterMDAKit(
        project_name=project_name,
        repo_name="mdakit-cookie",
        package_name="mdakit_cookie",
        github_username="test-user-account",
        github_host_account="MDAnalysis",
        description=description,
        dependency_source=dependency_source,
        include_ReadTheDocs=include_ReadTheDocs,
        output_directory=str(output_directory.resolve()),
    )
    kitter.run()
