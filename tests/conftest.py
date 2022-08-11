import pathlib
import pytest


@pytest.fixture
def test_output_directory(tmp_path, request):
    """A hack to decide if we want to keep outputs or not"""
    path = request.config.getoption("--keep-test-outputs")
    if path:
        path = pathlib.Path(path)
        path.mkdir(exist_ok=True)
        return path
    return tmp_path


def pytest_addoption(parser):
    parser.addoption(
        "--keep-test-outputs",
        action="store",
        default=None,
        help="Directory to keep test outputs",
    )
