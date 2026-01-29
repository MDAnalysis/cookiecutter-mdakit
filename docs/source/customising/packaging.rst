Packaging and Releases
======================

.. _packaging:

Packaging
---------
A ``pyproject.toml`` file has been created by the cookiecutter to allow your
code to be packaged and installed by users. This file has been automatically 
set up with relevant meta information, dependencies (both core and optional
dependencies for tests and documentaiton), and settings for additional features
including versioningit for :ref:`versioning your code <versioning>`.
You can edit this file to alter and of this information as appropriate.

A ``MANIFEST.in`` file is also created to identify additional files included 
when packaging your code (e.g., additional comminity information like the 
Code of Conduct).

Includion of ``pyproject.toml`` should mean your code is installable from GitHub.

It is also a good idea to upload your package onto a package repository such 
as `PyPI <https://pypi.org/>`_ or `conda-forge <https://conda-forge.org/>`_ to 
make installation even easier for your users. 

The `PyPI documentation <https://packaging.python.org/en/latest/tutorials/packaging-projects/>`_ 
contains instructions for creating distributions for your package and how to add
these to PyPI.  The initial steps - creation of relevant files - have been 
handled for you by the cookiecutter.
Once created, distribution files can also be used to 
`add your package to conda-forge <https://conda-forge.org/docs/maintainer/adding_pkgs/>`_.

As you develop your package, you should package and release new versions of your
code to give users access to the new features.


.. _version:

Versioning
----------
Tagging is a good way to keep references to a specific version of your code 
that won't change. This is especially useful when you want to a new a new code release. 
The ``cookiecutter`` uses `versioningit`_ to automatically determine your 
package's version based on git tags.

By default, the initial version has been set to ``0.0.0``. 
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

Once the new tag has been pushed to GitHub, you can 
`make a new release <https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository>`_ 
from this tag.

If using PyPI/Conda-forge, you should also upload the new releases here to these.

.. _versioningit: https://versioningit.readthedocs.io/en/stable/index.html
