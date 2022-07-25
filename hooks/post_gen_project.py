"""
Post Cookie Generation script(s)

These scripts are executed from the output folder.
If any error is raised, the cookie cutter creation fails and crashes
"""

import pathlib
import subprocess

COMMIT_MESSAGE = (
    "Initial creation with MDAnalysis Cookiecutter "
    "{{ cookiecutter._mda_cc_version }}"
)


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
        pathlib.Path("docs/requirements.yaml").unlink()
        pathlib.Path("readthedocs.yaml").unlink()


remove_rtd()
git_init_and_tag()
