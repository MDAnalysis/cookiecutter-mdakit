Making and pushing changes to your code
=======================================

.. _adding-code:

Now you should go forth and code!							

Your project's code will live in the ``{package_name}/`` directory. 
A basic ``__init__.py`` file (which :ref:`sets the version <versioning>`) as 
been pre-generated, along with several subpackages (and accompanying (empty)
``__init__.py``):

* ``analysis/``: If you chose to include a template analysis class when 
  running the cookiecutter, that class will appear in 
  ``{package_name}/anaylsis/{template_analysis_class}.py``. This class is based 
  on `MDAnalysis AnalysisBase <https://docs.mdanalysis.org/stable/documentation_pages/analysis/base.html>`_. 
  Comments in file should help you as you customise this class for your analysis.						
* ``tests/``: where your code's unit tests will live. See  :ref:`writing-tests`.

* ``data/``: for including additional (non-code) files with your package, such 
  as molecular structures; this may be useful for e.g. running tests. The 
  included ``data/README.md`` file provides more information. ``files.py`` 
  provides an example of how to set up files so they can be imported elsewhere
  in your package (useful especially if you wish to use the data in multiple 
  places), using the example datafile ``mda.txt``- containing ASCII art of the 
  MDAnalysis logo. The :ref:`example test files <writing-tests>` include an 
  example usage of this file.


Tips while writing your code
----------------------------
To keep things clean and simple, we advise a few tips:

.. _virtual-environment:

* Always work in a virtual environment like ``conda``.
  You can create a development environment by following
  the instructions in the README. In short, to create an environment that should contain
  all the tools you need to write and (locally) run tests and build documentation:


  .. code-block:: bash

    conda create --name <environment_name> python=3.8
    conda activate <environment_name>  # remember to do this every time
    conda env update --name <environment_name> --file devtools/conda-envs/test_env.yaml
    conda env update --name <environment_name> --file docs/requirements.yaml


* Always work in a separate branch. The ``main`` branch
  is the default, or central, branch. All development
  work should be done in a separate branch to avoid
  messing up the main branch, or to allow you to work on
  different approaches at the same time. This also
  allows multiple people to work on the code at the same time.
  Create a new branch with ``git checkout -b <my_branch_name>``.
  See `GitHub's documentation on branches <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches>`_
  for more information.

* When you feel ready, open a pull request on GitHub.
  **This does not have to be when you think you have finished the code!**
  A PR runs tests and builds documentation.
  This will allow others to review your code and
  help you make sure it is correct.
  It's always a good way to get feedback and validation,
  as well as collaborate with other people.
  See `GitHub's documentation on PRs <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests>`_
  for more information.
