Usage
=====

Getting up and running requires a short process.

You will need the following:
    * Python 3.8+
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

#. `Create a new repository on GitHub`_ .
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


Code quality analysis: LGTM
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Make a `LGTM`_ account and add your project.
If, desired you can add code review integration
by clicking the large green button!

Static code analysis dramatically enhances the quality of your code
by finding a large number of common mistakes that both novice and
advanced programmers make.
There are many static analysis codes on the market,
but we have seen that LGTM is a delicate balance between
verbosity and catching true errors.

The ``.lgtm.yml`` file contains configuration for LGTM.
Edit that file to modify settings.

.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _ReadTheDocs: https://readthedocs.org
.. _LGTM: https://lgtm.com
.. _`Create a new repository on GitHub`: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository

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
