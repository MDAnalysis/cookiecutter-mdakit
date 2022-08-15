.. MDAKits Cookiecutter documentation master file.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Cookiecutter for MDAnalysis-based packages
==========================================

**Cookiecutter-MDAKit version:** |Cookiecutter_MDAKit_version|

A `cookiecutter <https://github.com/audreyr/cookiecutter>`_ template
for those interested in developing packages
based on MDAnalysis.
Starting repositories can be created from this template so you can focus on what's important: the science!

**Features**

* Python-centric skeletal structure with initial module files
* Pre-configured ``setup.py`` for installation and packaging
* Pre-configured Window, Linux, and OSX continuous integration on GitHub Actions
* Choice of dependency locations through ``conda-forge``, default ``conda``, or ``pip``
* Basic testing structure with `PyTest <https://docs.pytest.org/en/latest/>`_
* Automatic ``git`` initialization + tag
* GitHub Hooks
* Automatic package version control with `Versioneer <https://github.com/warner/python-versioneer>`_
* Sample data inclusion with packaging instructions
* Basic documentation structure powered by `Sphinx <http://www.sphinx-doc.org/en/master/>`_


.. toctree::
   :maxdepth: 1
   :caption: General
   :hidden:
   
   usage
   options

.. toctree::
   :maxdepth: 1
   :caption: Developer
   :hidden:
   
   cookiecutter/json_options
   cookiecutter/hooks


Acknowledgments
===============
This cookiecutter is developed by MDAnalysis, based heavily off the `Cookiecutter for Computational Molecular Sciences (CMS) Python Packages <https://github.com/MolSSI/cookiecutter-cms>`_ by Levi N. Naden and Jessica A. Nash
from the `Molecular Sciences Software Institute (MolSSI) <http://molssi.org/>`_ and
Daniel G. A. Smith of `ENTOS <https://www.entos.ai/>`_.

The development of this repository is supported by a grant from the Chan Zuckerberg Initiative under an EOSS4 award.
