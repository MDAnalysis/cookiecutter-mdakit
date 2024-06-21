"""
Location of data files
======================

Use as ::

    from {{ cookiecutter.package_name }}.data.files import *

"""

__all__ = [
    "MDANALYSIS_LOGO",  # example file of MDAnalysis logo
]

import importlib.resources

data_directory = importlib.resources.files("{{ cookiecutter.package_name }}") / "tests" / "data"

MDANALYSIS_LOGO = data_directory / "mda.txt"
