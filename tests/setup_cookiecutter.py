#!/usr/bin/env python

import argparse
import pathlib
import subprocess


parser = argparse.ArgumentParser(description="Simulates a cookiecutter run")
parser.add_argument("--project", required=True, type=str, help="Project name")
parser.add_argument("--repo", default="", type=str, help="Repo name")
parser.add_argument("--account", required=True, type=str, help="Account name")
parser.add_argument("--github-url", default="", help="GitHub URL")
parser.add_argument("--module", default="", help="First module name")
parser.add_argument("--author", default="cookie monster", help="Author name")
parser.add_argument(
    "--author-email", default="cookiemonster@trash.can", help="Author email"
)
parser.add_argument("--description", default="", help="Description")
parser.add_argument(
    "--dependencies",
    required=True,
    choices=["1", "2", "3"],
    help="Dependencies",
)
parser.add_argument(
    "--rtd", required=True, choices=["1", "2"], help="ReadTheDocs"
)
parser.add_argument("--cookiecutter", default=".", help="Path to cookiecutter")
parser.add_argument("--verbose", action="store_true", help="Verbosity")


def run_cookiecutter(
    project: str = "",
    repo: str = "",
    account: str = "",
    github_url: str = "",
    module: str = "",
    author: str = "",
    author_email: str = "",
    description: str = "",
    dependencies: str = "",
    rtd: str = "",
    cookiecutter: str = ".",
    verbose: bool = False,
):
    cookiecutter = pathlib.Path(cookiecutter).resolve()

    options = [
        project,
        repo,
        account,
        github_url,
        module,
        author,
        author_email,
        description,
        dependencies,
        rtd,
    ]

    proc = subprocess.Popen(
        ["cookiecutter", str(cookiecutter)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    output = proc.communicate("\n".join(options).encode("UTF-8"))
    log = output[0].decode()
    log = "\n".join(log.split(": "))
    if verbose:
        print(log)

    if proc.returncode != 0:
        print(log)
        raise RuntimeError("Cookiecutter did not run successfully!")


if __name__ == "__main__":
    args = parser.parse_args()
    if args.verbose:
        print("Arguments")
        print(args)
    run_cookiecutter(**vars(args))
