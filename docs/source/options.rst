.. _options-label:

Options
=======

This page goes into the options you can choose in the cookiecutter,
what they mean, and what they affect.
If there are default values, they are explained.

project_name
------------

This is the name of the project you would
use when writing about it in the documentation.

repo_name
---------

This is the name of the directory containing
the package. It cannot contain spaces.
This value is used to generate the URL
to the project on GitHub
(i.e. ``github.com/<github_host_account>/<repo_name>``).

**Default value:** the ``project_name`` in lowercase,
with spaces and hyphens replaced with underscores.

package_name
------------

This is the name of the module you would use
when importing your package. It must
follow Python module naming rules, i.e. it cannot
have spaces or hyphens.

**Default value:** the ``repo_name`` in lowercase,
with spaces and hyphens replaced with underscores.

description
-----------

Give a short description of the project to appear in the README.

github_username
---------------

This should be your *personal* GitHub username.
It is used for giving you credit in AUTHORS.md.

github_host_account
-------------------

This should be the GitHub account name used to host the
repository. In most cases, this will be the same as
the GitHub username; however, if you are creating a
package for an organisation, use the organisation
account name. This value is used to generate the URL
to the project on GitHub
(i.e. ``github.com/<github_host_account>/<repo_name>``).

**Default value:** the ``github_username``.

author_name
-----------

This should be the name you prefer to go by, not your username.
It is used for giving you credit in files such as
``AUTHORS.md``, ``setup.py``, and other packaging materials.

author_email
------------

This should be an email address that you are comfortable
getting contacted at. It is used for contact details
in files such as ``AUTHORS.md``, ``setup.py``, and other packaging materials.
It is also used as the point of contact in ``CODE_OF_CONDUCT.md``.

dependency_source
-----------------

This option determines which sources to use for dependencies for the package.
It affects the continuous integration testing, as well as
the dependency files written. The three choices
(``conda-forge``, ``anaconda``, and ``pip``)
are explained below.

**Default value:** ``conda-forge``.


conda-forge
~~~~~~~~~~~

This option looks for dependencies first in the ``conda-forge`` channel,
then the default ``anaconda`` channel, before falling back to ``pip``.

.. note::

    We **highly recommend** using ``conda-forge``.
    ``conda`` is a great package manager for creating
    isolated environments, and managing dependencies between them.
    Moreover, many packages are available on ``conda-forge``
    that are not on the default ``anaconda`` channel or ``pip``.



anaconda
~~~~~~~~

This option still uses ``conda`` to manage dependencies,
but only uses the ``anaconda`` channel and ``pip`` fallback.
This option would install MDAnalysis from `PyPI`_ .
as it is not available on the default ``anaconda`` channel.

pip
~~~

This option only installs packages from `PyPI`_.


include_ReadTheDocs
-------------------

This option determines whether to include
ReadTheDocs configuration (``readthedocs.yaml``)
in the package. It does not affect the documentation itself.
We recommend keeping ReadTheDocs, as it is a standard and easy way
to automatically build documentation online.

**Default value:** "y" (True)


template_analysis_class
-----------------------

This option triggers the building of a skeleton custom
analysis class, and associated tests.
If a class name is given, it is used as the name of the
analysis class. If it is not given, this step is skipped.

We strongly encourage using this option if you are planning
to write custom analysis, as it copies a helpful
template with comments and notes to modify.

**Default value:** skip


.. _PyPI: https://pypi.org/
