"""
Post Cookie Generation script(s)

These scripts are executed from the output folder.
If any error is raised, the cookie cutter creation fails and crashes
"""

import pathlib
import shutil
import subprocess

COMMIT_MESSAGE = (
    "Initial creation with MDAnalysis Cookiecutter "
    "{{ cookiecutter._mda_cc_version }}"
)

LICENSE_OPTIONS = {
    "MIT": "MIT.txt",
    "GPL-3.0-or-later": "GPL-3.0.txt",
    "BSD-3-Clause": "BSD-3.txt",
    "Apache-2.0": "Apache-2.0.txt",
}


def remove_files(*paths):
    for path in paths:
        path = pathlib.Path(path)
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(str(path))
        else:
            raise ValueError(f"{path} is not a file or directory")


def run(command, expected_error=True, print_output=True) -> str:
    """Run a shell command and return the output."""
    try:
        proc = subprocess.run(command, shell=True,
                              text=True,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT,
                              )
    except subprocess.CalledProcessError as e:
        # Trap and print the output in a helpful way
        print(f"Return code: {proc.returncode}")
        print(proc.stdout)
        if not expected_error:
            raise e
    if print_output:
        print(proc.stdout)
    return proc.stdout


def git_init_and_tag():
    """
    Invoke the initial git and tag with 0.0.0 to make an initial version for
    Versioneer to ID if not already in a git repository.
    """

    # Check if we are in a git repository
    exists = run("git status", expected_error=True, print_output=False)

    # Create a repository and commit if not in one.
    if 'fatal' in exists:
        # Initialize git
        run("git init")
        # Change to main
        run("git checkout -b main")

        # Add files created by cookiecutter
        run("git add .")
        run(f"git commit -m '{COMMIT_MESSAGE}'")

        # Check for a tag
        version = run("git tag", expected_error=True)
        # Tag if no tag exists
        if not version:
            run("git tag 0.0.0")
    else:
        print("\ngit repository detected. ")

    print(
        "Cookiecutter files have been created in "
        "{{ cookiecutter.repo_name }} directory."
    )


def remove_rtd():
    """Remove the ReadTheDocs files if unnecessary."""
    include_rtd = '{{ cookiecutter.include_ReadTheDocs }}'
    if include_rtd == "n":
        remove_files("readthedocs.yaml")


def remove_analysis():
    """Remove analysis files if unnecessary. """
    include_analysis = '{{ cookiecutter.template_analysis_class }}'
    if not include_analysis:
        remove_files(
            "{{ cookiecutter.package_name }}/analysis",
            "{{ cookiecutter.package_name }}/tests/analysis"
        )


def remove_placeholder_icons():
    """Remove placeholder logos if unnecessary."""
    host_account = '{{ cookiecutter.github_host_account }}'
    if host_account.lower() == "mdanalysis":
        remove_files("docs/source/_static/logo")


def set_license():
    """Set LICENSE from template"""
    license_name = "{{ cookiecutter.license }}"
    repo_root = pathlib.Path.cwd()
    dest = repo_root / "LICENSE"
    licenses_dir = repo_root / "licenses"

    if license_name in LICENSE_OPTIONS:
        src = licenses_dir / LICENSE_OPTIONS[license_name]
        shutil.copy(src, dest)
    else:
        supported_licenses = ", ".join(LICENSE_OPTIONS.keys())
        raise ValueError(
            f"Unsupported license: {license_name!r}. "
            f"Supported licenses are: {supported_licenses}"
        )

    for filename in LICENSE_OPTIONS.values():
        path = licenses_dir / filename
        if path.is_file():
            path.unlink()

    if licenses_dir.is_dir():
        try:
            licenses_dir.rmdir()
        except OSError:
            pass


if __name__ == "__main__":
    set_license()
    remove_rtd()
    remove_analysis()
    remove_placeholder_icons()

    git_init_and_tag()
