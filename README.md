# Cookiecutter for MDAnalysis-based packages
[//]: # (Badges)
[![GitHub Actions Build Status](https://github.com/MDAnalysis/cookiecutter-mdakit/actions/workflows/gh-ci/badge.svg)](https://github.com/MDAnalysis/cookiecutter-mdakit/actions?query=workflow%3A%22Cookiecutter+CI%22)
[![Documentation Status](https://readthedocs.org/projects/cookiecutter-mdakit/badge/?version=latest)](https://cookiecutter-mdakit.readthedocs.io/en/latest/?badge=latest)


A [cookiecutter](https://github.com/audreyr/cookiecutter) template for those interested in developing
packages based on MDAnalysis. Skeletal starting repositories can be created from this template to create the
file structure semi-autonomously so you can focus on what's important: the science!

The skeletal structure is designed to help you get started, but do not feel limited by the skeleton's features
included here. Just to name a few things you can alter to suit your needs: change continuous integration options,
remove deployment platforms, or test with a different suite.

**Contents**
* [Features](#features)
* [Requirements](#requirements)
* [Usage](#usage)
* [Output Skeleton](#output-skeleton)
* [Setting up with GitHub](#setting-up-with-github)


## Features
* Python-centric skeletal structure with initial module files
* Pre-configured `setup.py` for installation and packaging
* Pre-configured Windows, Linux, and OSX continuous integration on GitHub Actions.
* Choice of dependency locations through `conda-forge`, default `conda`, or `pip`
* Basic testing structure with [PyTest](https://docs.pytest.org/en/latest/)
* Automatic `git` initialization + tag
* GitHub Hooks
* Automatic package version control with [Versioneer](https://github.com/warner/python-versioneer)
* Sample data inclusion with packaging instructions
* Basic documentation structure powered by [Sphinx](http://www.sphinx-doc.org/en/master/)

## Requirements

* Python 3.8+
* [Cookiecutter](http://cookiecutter.readthedocs.io/en/latest/installation.html)
* [Git](https://git-scm.com/)

## Usage

With [`cookiecutter` installed](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter),
execute the following command inside the folder you want to create the skeletal repository.

```bash
cookiecutter gh:MDAnalysis/cookiecutter-mdakit
```

Which fetches this repository from github automatically and prompts the user for some simple information such as
package name, author(s), and licences.

## Output Skeleton

This is the skeleton made by this `cookiecutter`. The items marked in `{{ }}` will be replaced by your choices
upon setup.

```
.                                      <- Directory created, named {{repo_name}}
├── AUTHORS.md                         <- List of all contributors to the package
├── CHANGELOG.md                       <- Log of changes in each release
├── CODE_OF_CONDUCT.md                 <- Code of Conduct for developers and users
├── CONTRIBUTING.md                    <- Guide to contributing
├── LICENSE                            <- License file
├── MANIFEST.in                        <- Packaging information for pip
├── README.md                          <- Description of project which GitHub will render
├── {{package_name}}
│   ├── __init__.py
│   ├── _version.py                    <- Automatic version control with Versioneer
│   ├── data                           <- Sample additional data (non-code) which can be packaged
│   │   ├── README.md
│   │   ├── __init__.py
│   │   ├── files.py                   <- Recommended file for resolving data file names
│   │   └── mda.txt                    <- Just an example, delete in production
│   ├── tests                          <- Unit test directory with sample tests
│   │   ├── __init__.py
│   │   ├── conftest.py                <- File for common pytest fixtures
│   │   └── test_{{package_name}}.py   <- Example test file
│   └── {{package_name}}.py            <- Starting package module
├── devtools                           <- Environment and other development tools
│   └── conda-envs                     <- Conda environments for testing
│       └── test_env.yaml
├── docs                               <- Documentation template folder with many settings already filled in
│   ├── Makefile
│   ├── README.md                      <- Instructions on how to build the docs
│   ├── _static
│   │   └── README.md
│   ├── _templates
│   │   └── README.md
│   ├── api.rst
│   ├── conf.py
│   ├── getting_started.rst
│   ├── index.rst
│   ├── make.bat
│   └── requirements.yaml              <- Documentation building specific requirements. Usually a smaller set than the main program
├── pyproject.toml                     <- Dependencies for pip
├── readthedocs.yaml                   <- Settings for ReadTheDocs
├── setup.cfg                          <- Near-master config file settings for Coverage, Flake8, YAPF, etc
├── setup.py                           <- Your package's setup file for installing with additional options that can be set
├── versioneer.py                      <- Automatic version control with Versioneer
├── .codecov.yml
├── .github                            <- GitHub hooks for user contribution, pull request guides and GitHub Actions CI
│   ├── ISSUE_TEMPLATE                 <- Templates for opening issues on GitHub
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   ├── PULL_REQUEST_TEMPLATE.md       <- Template for opening a pull request on GitHub
│   └── workflows
│       └── gh-ci.yaml
├── .gitignore                         <- Stock helper file telling git what file name patterns to ignore when adding files
├── .lgtm.yml                          <- Settings for LGTM.com
├── .pre-commit-config.yaml            <- Settings for pre-commit hooks for flake8 and isort
├── .pylintrc                          <- Settings for PyLint
```


## Setting up with GitHub
Upon creation, this project will initialize the output as a `git` repository compatible with
[Versioneer](https://github.com/warner/python-versioneer). However, this does not automatically register the
repository with GitHub. To do this, follow the instructions for
[Adding an existing project to GitHub using the command line](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/).
Follow the first step to create the repository on GitHub, but ignore the warnings about the README, license, and
`.gitignore` files as this repo creates them. From there, you can skip to after the "first commit" instructions and
proceed from there.

## Developing code

Now you're ready to develop some code!
We recommend developing in an isolated virtual environment.
Instructions for creating one are already given in your package README.



## Setting up external hooks

### ReadTheDocs (documentation)
Make a [ReadTheDocs](https://readthedocs.org) account and turn on the git hook. Although you can manually make the
documentation yourself through [Sphinx](http://www.sphinx-doc.org/en/master/usage/quickstart.html), you can also
configure [ReadTheDocs](https://docs.readthedocs.io/en/latest/getting_started.html) to automatically build and
publish the documentation for you. The initial skeleton of the documentation can be found in the `docs` folder
of your output.

We also advise turning on building documentation for pull requests, as a way to check and preview
your docs when you make changes.

### LGTM (code quality analysis)
Make a [LGTM](https://lgtm.com) account and add your project. If desired you can add code review integration by clicking the large green button!

Static code analysis dramatically enhances the quality of your code by finding a large number of common mistakes that both novice and advanced programmers make.
There are many static analysis codes on the market, but we have seen that LGTM is a delicate balance between verbosity and catching true errors.

### Codecov (test coverage)

Sign up at [Codecov](https://about.codecov.io/) and
[set up this repository](https://docs.codecov.com/docs/quick-start)
by adding the GitHub App Integration.
You may need to trigger some tests and wait a few hours
before seeing coverage reports appearing on Codecov.
You can use these reports to discover which parts of your code
are not checked by your current tests.
You should ideally aim for >90% code coverage to ensure that
your package actually does what you think it does!



## Acknowledgments

This cookiecutter is developed by MDAnalysis, based heavily off the
[Cookiecutter for Computational Molecular Sciences (CMS) Python Packages](https://github.com/MolSSI/cookiecutter-cms)
by Levi N. Naden and Jessica A. Nash
from the [Molecular Sciences Software Institute (MolSSI)](http://molssi.org/) and
Daniel G. A. Smith of [ENTOS](https://www.entos.ai/).
