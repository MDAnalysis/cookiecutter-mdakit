import subprocess
import pathlib
import tempfile
import os
import shutil
import re
from typing import List

import yaml

abs_filepath = pathlib.Path(__file__).resolve()
COOKIECUTTER_PATH = abs_filepath.parent.parent.parent
GENERATED_PATH = COOKIECUTTER_PATH / "docs" / "source" / "generated"


def flatten_dict(dct, key=tuple()):
    """Turn a nested dict into a flat dict, with keys as tuples."""
    for k, v in dct.items():
        fullkey = key + (k,)
        if isinstance(v, dict):
            yield from flatten_dict(v, fullkey)
        else:
            yield fullkey, v


def flatten_tree(lines: List[str]):
    """Turn tree lines into a flat dict of keys to mimic flatten_dict"""
    indent_patterns = [r"│  ", r"├──", r"└──", "│\xa0\xa0", "    "]

    flattened = []
    previous_key = tuple()
    previous_n_indent = 0
    for line in lines:
        n_indent = 0
        for pattern in indent_patterns:
            n_indent += len(re.findall(pattern, line))
            line = re.sub(pattern, "", line)
        if n_indent:
            if n_indent > previous_n_indent:
                flattened[-1] = flattened[-1] + ("__description",)
            key = previous_key[:n_indent-1] + (line.strip(),)
        else:
            key = tuple()
        flattened.append(key)
        previous_key = key
        previous_n_indent = n_indent
    return flattened


class FileDescriptions:
    def __init__(self):
        file_descriptions = abs_filepath.parent / "file_descriptions.yaml"
        with file_descriptions.open("r") as f:
            contents = yaml.safe_load(f)
        self.descriptions = contents
        self.flat_descriptions = dict(flatten_dict(contents))

    def label_files(self, output) -> str:
        lines = output.split("\n")
        flattened = flatten_tree(lines)
        with_labels = []
        n_max_char = 0
        arrow = "   <- "
        for line, key in zip(lines, flattened):
            value = self.flat_descriptions.get(key, "")
            if value:
                value = arrow + value
            with_labels.append((line, value))
            n_max_char = max(n_max_char, len(line))

        labelled_lines = []
        for line, value in with_labels:
            formatted = f"{line:<{n_max_char}}{value}"
            labelled_lines.append(formatted)
        return "\n".join(labelled_lines)


class ExampleRepositoryDocumentation:

    def __init__(self):
        self.repo_name = "example-repository"
        self.package_name = "package_name"
        self.example_repo_path = GENERATED_PATH / self.repo_name
        self.cookiecutter_cli_log = GENERATED_PATH / "cookiecutter_cli.log"
        self.cookie_tree = GENERATED_PATH / "cookie_tree.txt"

    def generate_cli_output(self) -> str:
        inputs = [
            "My Project Name",  # project_name
            self.repo_name,  # repo_name
            self.package_name,  # package_name
            "A package to do MD analysis",  # description
            "my-github-username",  # github_username,
            "",  # github_host_account
            "My Name",  # author_name
            "my_example_email@gmail.com",  # author_email
            "",  # dependency_source
            "",  # include_ReadTheDocs
            "MyAnalysisClass",  # template_analysis_class
            ""
            ""
        ]

        with tempfile.TemporaryDirectory() as tmpdir:
            proc = subprocess.run(
                # splitting out the "." means it's ignored for some reason
                f"cookiecutter {str(COOKIECUTTER_PATH)}",
                shell=True,
                text=True,
                capture_output=True,
                input="\n".join(inputs),
                cwd=tmpdir,
            )
            source_repo = os.path.join(tmpdir, self.repo_name)
            destination_repo = str(self.example_repo_path.resolve())
            shutil.rmtree(destination_repo, ignore_errors=True)
            shutil.copytree(source_repo, destination_repo)

        output = proc.stdout.split(": ")
        log = [f"{prompt}: {value}" for prompt, value in zip(output, inputs)]
        # not sure why this happens -- git not configured?
        if log[-1].strip().endswith("hint:"):
            log = log[:-1]

        logtext = "\n".join(log)
        logtext = "$ cookiecutter gh:MDAnalysis/cookiecutter-mdakit\n" + logtext
        return logtext

    def write_cookiecutter_cli_log(self):
        output = self.generate_cli_output()
        with self.cookiecutter_cli_log.open("w") as f:
            f.write(output)
        print(f"Wrote {self.cookiecutter_cli_log}")

    def write_cookie_tree(self):
        proc = subprocess.run(
            f"tree -I .git -a {self.repo_name}",
            shell=True,
            cwd=GENERATED_PATH,
            capture_output=True,
            text=True
        )
        tree = proc.stdout
        descriptions = FileDescriptions()
        formatted = descriptions.label_files(tree)

        with self.cookie_tree.open("w") as f:
            f.write(formatted)
        print(f"Wrote {self.cookie_tree}")

    def run(self):
        self.write_cookiecutter_cli_log()
        self.write_cookie_tree()


def main():
    docs = ExampleRepositoryDocumentation()
    docs.run()


if __name__ == "__main__":
    main()
