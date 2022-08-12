import ast
import enum
from dataclasses import dataclass, asdict
import pathlib
from typing import Literal, List

from cookiecutter.main import cookiecutter

COOKIECUTTER_PATH = pathlib.Path(__file__).parent.parent.resolve()


def get_classes_from_file(path: str) -> List:
    path = pathlib.Path(path)
    with path.open() as f:
        tree = ast.parse(f.read(), filename=str(path))

    classes: List[str] = []
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.ClassDef):
            classes.append(node.name)
    return classes


IncludeReadTheDocs = Literal["y", "n"]


class DependencyType(enum.Enum):
    CONDAFORGE = "Prefer conda-forge over the default anaconda channel with pip fallback"
    ANACONDA = "Prefer default anaconda channel with pip fallback"
    PIP = "Dependencies from pip only (no conda)"


@dataclass
class CookiecutterMDAKit:
    project_name: str = "TestMDAKitProjectName"
    repo_name: str = "test-mda-kit"
    package_name: str = "test_mdakit_package"
    github_username: str = "test-user-account"
    github_host_account: str = "test-github-host-account"
    author_name: str = "Test User name"
    author_email: str = "test_email@test.com"
    description: str = "Test MDAKit Project description"
    dependency_source: DependencyType = DependencyType.CONDAFORGE
    include_ReadTheDocs: IncludeReadTheDocs = "y"
    template_analysis_class: str = "MyAnalysisClass"
    output_directory: str = "."

    @property
    def cookie_directory(self) -> pathlib.Path:
        return pathlib.Path(self.repo_name)

    @property
    def package_directory(self) -> pathlib.Path:
        return self.cookie_directory / self.package_name

    def run(self):
        context = {}
        for k, v in asdict(self).items():
            if isinstance(v, enum.Enum):
                v = v.value
            context[k] = v

        return cookiecutter(
            str(COOKIECUTTER_PATH),
            no_input=True,
            extra_context=context,
            output_dir=self.output_directory,
        )

    def cookie_path_exists(self, path: str) -> bool:
        path = self.cookie_directory / path
        return path.exists()

    def cookie_package_path_exists(self, path: str) -> bool:
        path = self.package_directory / path
        return path.exists()

    def get_classes_from_package_file(self, path: str) -> List[str]:
        path = self.package_directory / path
        return get_classes_from_file(path)
