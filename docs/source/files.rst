.. _files-label:

Files Overview
===============
The MDAKit cookiecutter generated a large number of files, which can be 
daunting. However, many do no require editing or input from you, or are only 
required to make use of optional features.

The table below provides a summart of the generated files, (this links to the 
relevant sections of documentation), and an indication of if the file is 
"required" or likely to require modification.

**Is this file 'required'?**

There are several ways one could consider defining a 'required file'. The table below uses the
follow classifications:

* **YES** - files that are central to your Python package being a Python package
* **REGISTRATION REQUIREMENT** - files that are not required for the package to work, but are required if you wish to register your MDAKit on the Registry
* **RECOMMENDED** - files that provide additional options not required for MDAKit registration, but that are still recommended for a good software package. Some of these are required in order for certain (optional) features to work; these are noted
* **OPTIONAL** - other files that may still be useful
* **NO** - files that are included only for illustative purposes or to guide you (the developer)


**Will I need to modify this file?**

* **YES** - files that (if you keep) you'll have to change
* **PROJECT DEPENDENT** - files that will need to be modified in some, but not all cases
* **OPTIONAL** - files that you can opt to edit to e.g. replace default selections or add additional customisation
* **NO** - files where it's unlikely you'll need to change any options, or that you shouldn't touch at all (unless you know what you're doing)


.. list-table:: Cookiecutter files
   :widths: 10 10 35 15 15 
   :header-rows: 1

   * - Name
     - Category
     - Description
     - "Required?"
     - Modify?
   * - ``LICENSE``
     - :ref:`GENERAL INFORMATION <general-info>`
     - File containing the details of the GPLv2 license, the default license for packages developed from the MDAKit cookiecutter
     - **YES** - without a clear license, *no-one* can legally use your code
     - **OPTIONAL** - you can opt for a license other than GPLv2
   * - ``README.md``
     - :ref:`GENERAL INFORMATION <general-info>`
     - A basic introduction/overview of the package; this file will be rendered on the GitHub repo's home
     - **REGISTRATION REQUIREMENT** - this is the minimum form of documentation your project should have
     - **OPTIONAL** - ammend as you suits your project
   * - ``CODE_OF_CONDUCT.md``
     - :ref:`COMMUNITY <community-resources>`
     - Rules for behaviour for all members of the project's community (users and developers).
     - **RECOMMENDED** - setting clear rules and expectations is the foundation for a healthy community
     - **OPTIONAL** - ammend as you suits your project
   * - ``CONTRIBUTING.md``
     - :ref:`COMMUNITY <community-resources>`
     - Basic guide and instructions for those considering conbribution to the project
     - **RECOMMENDED** - providing a guide to contributing will lower the entry barrier for first-time contributors to your project
     - **OPTIONAL** - ammend as you suits your project
   * - ``AUTHORS.md``
     - :ref:`DOCUMENTING CHANGES <documenting-changes>`
     - List of all contributors to the project
     - **RECOMMENDED** - tracking all contributors to your project is important for giving credit
     - **YES** - this file will be ammended whenever there is a new contributor
   * - ``CHANGELOG.md``
     - :ref:`DOCUMENTING CHANGES <documenting-changes>`
     - Curated log of notable changes (and corresponding versions) made as the package is developed
     - **RECOMMENDED** - keeping a changelog lets both developers and users know what major changes have been introduced and when
     - **YES** - this file will be ammended whenever a notable change is made to the project
   * - ``.gitignore``
     - :ref:`VERSION CONTROL`
     - Stock helper file telling git what file name patters to ignore when adding files
     - **RECOMMENDED** - this will reduce clutter in your commit history
     - **NO** - this is a stock file that should cover all likely cases
   * - ``.github/``
     - :ref:`GITHUB FEATURES <github-features>`
     - *Files for options GitHub features*
     - 
     - 
   * - ``.github/workflows/``
     - :ref:`GITHUB FEATURES <github-features>`
     - *Workflow confugration files for running automated processes using GitHub actions*
     - *RECOMMENDED - having at least a CI workflow to automate tests and checks is recommended*
     - *OPTIONAL - you can opt to add additional GitHub Actions workflows here*
   * - ``.github/ISSUE_TEMPLATE/``
     - :ref:`GITHUB FEATURES <github-features>`
     - *Templates for GitHub Issues*
     - *RECOMMENDED - template issues files will likely make things easier for both issue raisers and responders*
     - *NO - the standard templates are already included, though you may also add custom templates*
   * - ``.github/ISSUE_TEMPLATE/bug_report.md``
     - :ref:`GITHUB FEATURES <github-features>`
     - Template that will be provided to contributors when making a "bug report" issue on GitHub
     - **RECOMMENDED** - templates will likely make things easier for both you and the contributor
     - **NO** - this is a standard template unlikely to need changing, though you can modify it if you wish
   * - ``.github/ISSUE_TEMPLATE/feature_request.md``
     - :ref:`GITHUB FEATURES <github-features>`
     - Template that will be provided to contributors  when making a "feature request" issue on GitHub
     - **RECOMMENDED** - templates will likely make things easier for both you and the contributor
     - **NO** - this is a standard template unlikely to need changing, though you can modify it if you wish
   * - ``.github/PULL_REQUEST_TEMPLATE.md``
     - :ref:`GITHUB FEATURES <github-features>`
     - Template that will be provided to contributors when making a "Pull Requestion" on GitHub
     - **RECOMMENDED** - templates will likely make things easier for both you and the contributor
     - **NO** - this is a standard template unlikely to need changing, though you can modify it if you wish
   * - ``{package_name}/``
     - :ref:`CODE <adding-code>`
     - *The import pacakge, containing your project's code*
     - *YES - this is where your code itself will live*
     - **YES** - you'll need to add your own code!
   * - ``{package_name}/__init__.py``
     - :ref:`CODE <adding-code>`
     - __init__.py file to mark your code package
     - **YES** - this allows ``{package_name}`` to be imported (and sets your code's version)
     - **PROJECT DEPENDENT** - you may wish to add 
   * - ``{package_name}/analysis/``
     - :ref:`CODE <adding-code>`
     - *(Optional, only created if ' template analysis class' is selected) Directory for analysis code; set up with an (empty) __init__ .py*
     - *NO - you do not have to follow the initial generated subpackage structure*
     - *YES - if you opt to keep this cookiecutter-generated subpackage, you'll need to add your own code here!*
   * - ``{package_name}/analysis/{class_name}.py``
     - :ref:`CODE <adding-code>`
     - (Optional, only created if ' template analysis class' is selected) File containing a template analysis class, based off  MDAnalysis; ``AnalysisBase``.
     - **RECOMMENDED** - if your code features a frame-by-brame timeseries analysis, it is highly recommended to start with a Class based on ``AnalysisBase``.
     - **YES** - if using this template, you'll need to add your own code here!
   * - ``{package_name}/data/``
     - :ref:`CODE <adding-code>`
     - *Subpackage for including additional (non-code) date to be included in the package; set up with an empty ``__init__.py`` file*
     - *NO - this subpackage demonstrates how additional non-code files can be included, but is not required*
     - *OPTIONAL - if you do wish to include non-code data, you'll add them here*
   * - ``{package_name}/data/README.md``
     - :ref:`CODE <adding-code>`
     - Additional information for including non-code files with your package
     - **NO** - but you may wish to refer to this file in future, so keep it around
     - **NO** - the purpose of this file is only to provide information to you, the devloper
   * - ``{package_name}/data/files.py``
     - :ref:`CODE <adding-code>`
     - Module for setting up non-code files to be imported elsewhere in the package
     - **OPTIONAL** - a central file to set up importing of your non-coding will likely make things easier
     - **YES** - if you opt to include non-code datafiles this way, you'll need to add them here
   * - ``{package_name}/data/mda.txt``
     - :ref:`CODE <adding-code>`
     - An example data file (ASCII art of the MDAnalysis logo) to demonstrate inclusion of non-code data
     - **NO** - this file is only for illustrative purposes
     - **NO** - this file is only for illustrative purposes
   * - ``devtools/``
     - *Misc.*
     - 
     - 
     - 
   * - ``devtools/conda-envs/``
     - *Misc.*
     - 
     - 
     - 
   * - ``{package_name}/tests/``
     - :ref:`TESTING <writing-tests>`
     - *Directory for unit tests. Set up with an empty ``__init__.py``*
     - *REGISTRATION REQUIREMENT - your MDAKit must have at least basic tests to be Registered!*
     - *YES - you'll need to add your own tests!*
   * - ``{package_name}/tests/conftest.py``
     - :ref:`TESTING <writing-tests>`
     - File to set up pytest fixtures for use in your tests, containing an example fixture
     - **OPTIONAL** - The example fixture can be removed, but fixtures are a very useful feature of pytest; if you have multiple fixtures/used in multiple places, keeping them in a separate file will help keep your tests organised
     - **PROJECT DEPENDENT** - The example fixture can be removed, but whether you have fixtures to include here depend on your projects
   * - ``{package_name}/tests/test_{package_name}.py``
     - :ref:`TESTING <writing-tests>`
     - Initial test module for your package with pytest, containing  sample tests
     - **REGISTRATION REQUIREMENT** - to be registered, your MDAKit needs at least basic unit tests, which will live here (though note you can rename or rearrange this file)
     - **YES** - add your tests here! The initial sample tests can be removed
   * - ``{package_name}/tests/utils.py``
     - :ref:`TESTING <writing-tests>`
     - Utility file for setting up other code useful for your tests, containing an example class for setting up a dummy Universe
     - **OPTIONAL** - A separate file for setting up common utilities can help keep your tests more organised
     - **PROJECT DEPENDENT** - The example fixture can be removed, but whether you have fixtures to include here depend on your projects
   * - ``{package_name}/tests/analysis/``
     - :ref:`TESTING <writing-tests>`
     - (Optional, only created if ' template analysis class' is selected) Subpackage for test on the package's analysis class; set up with empty ``__init__.py``.
     - *NO - you do not have to follow the initial generated subpackage structure*
     - *YES - if you opt to keep this cookiecutter-generated subpackage, you'll need to add your tests code here!*
   * - ``{package_name}/tests/analysis/test_{analysis_class}.py``
     - :ref:`TESTING <writing-tests>`
     - (Optional, only created if ' template analysis class' is selected) Example module with initial framework for tests on the package's analysis class using pytest
     - **RECOMMENDED** - if your code features a frame-by-frame anaysis based on AnalysisBase, this file is a good place to start for writing your tests
     - *YES - if you opt to keep this cookiecutter-generated subpackage, you'll need to add your tests code here!*
   * - ``devtools/conda-envs/test_env.yaml``
     - :ref:`TESTING <running-tests>`
     - A configuration file for creating an environment with the required dependencies for running the project's tests using pytest
     - **YES** - this will allow you to set up an environemnt with the tools needed to run your tests locally
     - **PROJECT DEPENDENT** - you may need to modify this file if your tests have additional dependencies
   * - ``.github/workflows/gh-ci.yaml``
     - :ref:`CONTINUOUS INTEGRATION <continuous-integration>`
     - A configuration file specifying steps for running Continuous Integration, using `GitHub Actions <https://docs.github.com/en/actions>`_ 
     - **RECOMMENDED (required for CI)** - many checks can be run manually, but having them run automatically through CI will make your (and other contributors') lives easier
     - **OPTIONAL** -  if you know what you're doing, you can add additional CI checks and change settings in this file
   * - ``.codecov.yml``
     - :ref:`TESTING (code coverage) <running-tests>`
     - Settings for `Codecov <https://about.codecov.io/>`_, a test coverage reporting tool
     - **OPTIONAL** - this file provides additional options for configuration, but is not required for running codecov
     - **OPTIONAL** - adjust this file to suit your preferences
   * - ``docs/``
     - :ref:`DOCUMENTATION <add-docs>`
     - *Configuration files and template source files for building a User Guide using Sphinx*
     - *RECOMMENDED - a README.md provides a minimal level of documentation, but a User Guide offering more details is highly recommended*
     - *YES - if you opt to create a User Guide using Sphinx, you can add your documentation information here*
   * - ``docs/source/``
     - :ref:`DOCUMENTATION <documentation-writing>`
     - *Source files for building documentation using Sphinx*
     - *RECOMMENDED (required for building documentation with Sphinx)*
     - *YES - if you opt to build your User Guide using Sphinx, you'll add your documentation here*
   * - ``docs/source/index.rst``
     - :ref:`DOCUMENTATION <documentation-writing>`
     - Home page for your project's User Guide, generated using Sphinx
     - **RECOMMENDED (required for building documentaiton using Sphinx)** - if you build a User Guide using Sphinx, you'll need at least this home page
     - **YES** - add details here as appropriate for your project
   * - ``docs/source/getting_started.rst``
     - :ref:`DOCUMENTATION <documentation-writing>`
     - Stub page for User Guide-style documentation on your project's User Guide, generated using Sphinx
     - **RECOMMENDED** - providing users with details on how to get started using your package is highly recommended
     - **OPTIONAL** - but you need not follow the autogenerated file structure
   * - ``docs/source/api.rst``
     - :ref:`DOCUMENTATION <documentation-writing>`
     - Stub page for API-stype documentation on your project's User Guide, generated using Sphinx
     - **RECOMMENDED** - providing users with an API guide is highly recommended
     - **OPTIONAL** - including API-style docs is recommended, but you need 
   * - ``docs/source/conf.py``
     - :ref:`DOCUMENTATION <documentation-configuration>`
     - Configuration file for building documentation using Sphinx
     - **RECOMMENDED (required if using Sphinx)** 
     - **OPTIONAL** - you can alter this file to customise your documentation
   * - ``docs/source/_static/``
     - :ref:`DOCUMENTATION <documentation-configuration>`
     - Static files for customising your documentation, such as logos and style sheets; see the encloded ``REAMDE`` for more information.
     - *OPTIONAL*
     - *OPTIONAL - you can add files here to customise your documentation*
   * - ``docs/source/_templates/``
     - :ref:`DOCUMENTATION <documentation-configuration>`
     - Template files for customising your documentation; see the encloded ``REAMDE`` for more information.
     - *OPTIONAL*
     - *OPTIONAL - you can add files here to customise your documentation*
   * - ``docs/source/_static/logos/``
     - :ref:`DOCUMENTATION <documentation-configuration>`
     - Placeholer and template logo files for MDAKits
     - *OPTIONAL*
     - *OPTIONAL - you can add files here to customise your documentation*
   * - ``docs/source/_static/logos/mdakits-empty-favicon-template.svg``
     - :ref:`DOCUMENTATION <documentation-configuration>`
     - Placeholder favicon for the User Guide documentaiton
     - *OPTIONAL*
     - *OPTIONAL - you can alter this file to customise your documentation*
   * - ``docs/source/_static/logos/mdakits-empty-logo-template.svg``
     - :ref:`DOCUMENTATION <documentation-configuration>`
     - Template "empty gears" MDAKits logo file, which you can edit to make your own logo
     - **NO** - this file is here to provide you with a template to edit, if you wish
     - *OPTIONAL - you can alter this file to customise your documentation*
   * - ``docs/source/_static/logos/mdakits-placeholder-logo.png``
     - :ref:`DOCUMENTATION <documentation-configuration>`
     - Placeholder logo for the User Guide documentation
     - *OPTIONAL*
     - *OPTIONAL - you can alter this file to customise your documentation*
   * - ``docs/README.md``
     - :ref:`DOCUMENTATION <documentation-building>`
     - Reference file containing instructions for building the documentaiton
     - **NO** - this file is for your reference (but you might want to view it later, so keep it around)
     - **NO** - this file serves only as a reference for developers
   * - ``docs/requirements.yaml``
     - :ref:`DOCUMENTATION <documentation-building>`
     - Configuration file listing the depencencies for building the documentation
     - **OPTIONAL (required if you want to build documentaiton locally/with ReadTheDocs)**
     - **PROJECT DEPENDENT** - if your documentation has additional dependencies, you'll need to add them here
   * - ``docs/Makefile``
     - :ref:`DOCUMENTATION <documentation-building>`
     - Confiugration file for building documentation using Sphinx
     - **OPTIONAL (required if you want to build documentaiton locally/with ReadTheDocs)**
     - **NO** - you shouldn't need to touch this file
   * - ``docs/make.bat``
     - :ref:`DOCUMENTATION <documentation-building>`
     - Script file for building documentation using Sphinx
     - **OPTIONAL (required if you want to build documentaiton locally/with ReadTheDocs)**
     - **NO** - you shouldn't need to touch this file
   * - ``readthedocs.yaml``
     - :ref:`DOCUMENTATION <documentation-hosting>`
     - Settings for `ReadTheDocs <https://docs.readthedocs.io/en/stable/>`_, a tool for building and hosting documentation
     - **OPTIONAL (required if you want to use ReadTheDocs)**
     - **NO** - not likely, unless you know what you're doing
   * - ``pyproject.toml``
     - :ref:`PACKAGING <packaging>`
     - Configuration file for the Python package
     - **YES** - this is the main configuration file for your package and required for users to be able to isntall your code
     - **PROJECT DEPENDENT** - 
   * - ``MANIFEST.in``
     - :ref:`PACKAGING <packaging>`
     - List of additional files to include (or exclude) when packaging code for distrubution
     - **NO** - most key files will be included by default
     - **NO** - 
   * - ``.pre-commit-config.yaml``
     - CODE (style checking)
     - Settings for pre-commit hooks to run formatting and linting checks on your code
     - **OPTIONAL** - pre-commit hooks can be useful for finding stylistic errors in your code before making commits, but are not required
     - **OPTIONAL** - you can change settings in this file as descired
   * - ``.pylintrc``
     - CODE (style checing)
     - Settings for `PyLint <https://pylint.readthedocs.io/en/stable/>`_
     - **OPTIONAL (required to run PyLint)**
     - **OPTIONAL** - you can change settings in this file as descired
