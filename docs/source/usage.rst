Usage
=====

Getting up and running requires a short process.

You will need the following:
  * Python 3.9+
  * The `cookiecutter`_ tool installed
  * A GitHub account


1. Use the cookiecutter to create a new project
------------------------------------------------

An example of using the cookiecutter is illustrated below.
The first line is the prompt, i.e. the actual
command to use. It is followed by all the prompts you can expect,
and some example answers.

.. literalinclude:: generated/cookiecutter_cli.log
    :language: bash


This generates the output skeleton:

.. literalinclude:: generated/cookie_tree.txt

We will go more into these files in the rest of this
tutorial, as well as other sections in this documentation.
Please see :ref:`options-label` for more details.

2. Add the project to GitHub
----------------------------

The generated repository should be an initialised git repository.
We now need to connect it to GitHub:

#. `Create a new repository on GitHub <https://docs.github.com/en/get-started/quickstart/create-a-repo>`_ .
   Do not initialize the repo with a README, license, or any other files.
#. Push the local repository to GitHub.
   GitHub should provide instructions for doing so, but in short:

   * Add the remote named ``origin`` with :code:`git remote add origin <URL>`
   * Push the local repository to the remote repository with :code:`git push -u origin main`
   * Verify files were pushed successfully by checking on GitHub

3. Link external hooks
----------------------

The generated repository contains configuration files for several
external services. These need to be manually linked to each service to run.

Documentation: ReadTheDocs
~~~~~~~~~~~~~~~~~~~~~~~~~~

ReadTheDocs builds documentation automatically for you from the files in ``docs/``.
(See more in the section on **Documentation**.)
To link ReadTheDocs, ensure that you have a `ReadTheDocs`_ account;
you should be able to use your GitHub account. To link the project,
click the ``Import a Project`` button on the dashboard.

We strongly recommend turning on building documentation for your
pull requests to check and preview your docs. To do so:

#. Go to the Admin tab
#. Go to Advanced Settings
#. Tick the "Build pull requests for this project" checkbox
#. Scroll down and remember to click "Save"!

Further configuration can be done on `ReadTheDocs`_
or in the ``readthedocs.yaml`` file.


Test coverage: Codecov
~~~~~~~~~~~~~~~~~~~~~~

Sign up at `Codecov <https://about.codecov.io/>`_ and
`set up this repository <https://docs.codecov.com/docs/quick-start>`_
by adding the GitHub App Integration.
You may need to trigger some tests and wait a few hours
before seeing coverage reports appearing on Codecov.
You can use these reports to discover which parts of your code
are not checked by your current tests.
You should ideally aim for >90% code coverage to ensure that
your package actually does what you think it does!

The ``.codecov.yml`` file contains configuration for Codecov.
Edit that file to modify settings, such as files to ignore
and what to include in the coverage report.

4. Make and push changes to your code
-------------------------------------

Now you should go forth and code!
To keep things clean and simple, we advise a few tips:

* Always work in a virtual environment like ``conda``.
  You can create a development environment by following
  the instructions in the README. In short:

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


5. Set up documentation
-----------------------

Documentation is important for your users and for yourself.

The documentation is built using `Sphinx <https://www.sphinx-doc.org/en/master/>`_.

Generally, a project will have a few types of documentation:

  * User guide-type documentation, which explains how and why to use the package.
    While it may contain code examples, it's typically more of a broad
    overview of package usage. 
    For example, this page is user-guide-like documentation.
    A stub page for user-guide-like documentation is created in
    ``docs/source/getting_started.rst``.

  * API documentation, which explains how to use the code.
    This is often automatically generated from docstrings in the code.
    A stub page for API documentation is created in
    ``docs/source/api.rst``.


Documentation configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The documentation is configured in the ``docs/source/conf.py`` file.
This file contains settings for the documentation, such as the
project name, version, and theme. You can also add extensions
to the documentation.
More information on configuring Sphinx can be found in the
`Sphinx documentation <https://www.sphinx-doc.org/en/master/usage/configuration.html>`_.

By default, the documentation is built using the MDAnalysis theme
sphinx theme using the default template MDAKits logo and `favicon`_.
You can change the theme by modifying the ``html_theme`` variable in
``docs/source/conf.py``.
You can also change the logo by either modifying the
``html_logo`` variable or by replacing the
``_static/logo/mdakits-placeholder-logo.png`` file.
(This path is relative to the ``docs/source`` directory;
the full path, relative to the repository root, is
``docs/source/_static/logo/mdakits-placeholder-logo.png``.)

Similarly, you can change the favicon by replacing the
``html_favicon`` variable or by replacing the
``_static/logo/mdakits-empty-favicon-template.svg`` file.

You are welcome to either create an entirely custom logo
and favicon or to use the provided templates.
An ``mdakits-empty-logo-template.svg`` and
``mdakits-empty-favicon-template.svg`` are provided in the
``docs/source/_static/logo`` directory as templates for
editing -- feel free to place your logo within the gears!

Building the documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~

To build the documentation, you can use the following command:

.. code-block:: bash

  $ cd docs
  $ make html

This will build the documentation in the ``docs/build/html`` directory.


6. Tagging versions of your code
--------------------------------

Tagging versions of your code is a good way to keep references
to specific versions of your code that don't change.
This is especially useful when you want to make a new code
release. The ``cookiecutter`` uses `versioningit`_ to
automatically determine your package's version based on
git tags.

By default, versioning will start from ``0.0.0``.
You can install versioningit_ to check the current versioningit output from commandline:

.. code-block:: bash
  
  $ cd <my_package_directory>
  $ versioningit .
  0.0.0

As you add commits, the versioning will automatically update with
the commit hashes:

.. code-block:: bash

  $ versioningit .
  0.0.0+1.g58bcaff

To tag a version, use the following command:

.. code-block:: bash

    git tag -a 0.1.0 -m "Version 0.1.0"

This will create a tag called ``0.1.0`` with the message
"Version 0.1.0". You can then push this tag to GitHub with ``git push origin --tags``.

After creating a tag, you can check the versioning again:

.. code-block:: bash

  $ versioningit .
  0.1.0


.. _ReadTheDocs: https://docs.readthedocs.io/en/stable/index.html
.. _cookiecutter: https://cookiecutter.readthedocs.io/en/stable/
.. _versioningit: https://versioningit.readthedocs.io/en/stable/index.html
.. _favicon: https://en.wikipedia.org/wiki/Favicon