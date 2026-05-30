Testing and Continuous Integration
==================================

.. _writing-tests:

Writing tests with Pytest
-------------------------
A subpackage ``{package_name}/tests/`` is provided for you to add your tests.
The cookiecutter uses `pytest <https://docs.pytest.org>`_; read the 
`pytest documentation <https://docs.pytest.org/en/stable/how-to/assert.html>`_ 
for more information on writing tests with pytest.

The generated ``tests/`` subpackage includes several template files and examples 
to get you stated:

* ``conftest.py``, which demonstrates creation of a 
  `fixture <https://docs.pytest.org/en/stable/explanation/fixtures.html>`_ using 
  the example MDAnalysis logo datafile
* ``test_{package_name}.py``: an initial test module, where you add the tests 
  themselves, with initial sample tests for checking your package can be imported 
  and a basic test using the MDAnalysis logo picture setup up in ``conftest.py``
* ``utils.py``: a utility file for other code useful for your tests, containing a 
  class for creating a dummy MDAnalysis Universe.

If you opted to include a template analysis class when using the cookiecutter, an 
``analysis`` subpackge is also created, containing a 
``test_{template_analysis_class}.py`` module with initial framework for checking 
your analysis class with a dummy universe.

.. _running-tests:

Running tests with Pytest
-------------------------
Running pytest requires additional dependencies. 
``devtools/conta-denvs/test_env.yaml`` specifies the initial dependencies, 
allowing you to easily :ref:`add them to your virtual environment <virtual-environment>`.

Tests can then be run locally using:

Depending on your project, you may end up with additional dependentices for 
your tests; add them in both ``test_env.yaml`` and ``pyproject.toml``.


.. _continuous-integration:

Running Continuous Integration with GitHub Actions
--------------------------------------------------

Continuous Integration (CI) for your project has been set up via a 
`GitHub actions <https://docs.github.com/en/actions>`_ workflow in 
``.github/workflows/gh-ci.yaml``. This CI should begin automatically once the 
code is on GitHub, and will run when you push changes to the main branch, a Pull
Request is made, and on a once-weekly schedule.

The provided CI workflow include checks for:

* running Pytest on with various combinations of operating system (ubuntu, 
  macOS, windows), Python versions, and MDAnalysis version ('latest' and 'develop')
* hooks to generate test coverage reports with `CodeCov <https://about.codecov.io/>`_ 
  (further setup required, see :ref:`test-covereage`)
* a code formatting check using `Pylint <https://www.pylint.org/>`_
* a test to see if a source distribution can be built

CI results will appear in the ``Actions`` tab on GitHub or in the PR, as appropriate.

.. _test-coverage:

Test coverage with Codecov
--------------------------

The MDAKits cookiecutter uses CodeCov for test coverage reporting. 
To make use of this feature, you will first need to sign up at 
`Codecov <https://about.codecov.io/>`_ and follow the instructions to 
`set up this repository <https://docs.codecov.com/docs/quick-start>`_
by adding the GitHub App Integration (Steps 1 and 2). 
Uploading of the coverage report (Step 4) is already provided by the 
:ref:`cookiecutter generated CI <continuous-integration>`.  

You may need to trigger some tests (e.g. by pushing to the GitHub repository) 
and wait a few hours before seeing coverage reports appearing on Codecov.
You can use these reports (also visible from the `Actions` tab on GitHub and 
in your PRs) to discover which parts of your code
are not checked by your current tests.
**You should ideally aim for >90% code coverage to ensure that
your package actually does what you think it does!**

The ``.codecov.yml`` file contains configuration for Codecov.
Edit that file to modify settings, such as files to ignore
and what to include in the coverage report.
See the `Codecov docs <https://docs.codecov.com/docs/codecov-yaml>`_ for more information.

