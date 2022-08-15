cookiecutter.json
=================

``cookiecutter.json`` contains the prompts used for the cookiecutter.
As JSON does not allow comments, here are some notes:

Format
------

Each key is the variable name; each value is the **default value**.
This severely limits how informative a prompt can be,
if we want to support a default value.

Some values are Jinja variables that are rendered on the spot.

dependency_source
-----------------

We ask users to choose which dependency source to use here.
However, each option is very verbose so users know what they are in for.
That can be quite annoying to work with in the resulting project.

Therefore, the ``cookiecutter.dependency_source`` variable
should not be used for the sake of simplicity.

Later in the JSON file, we use the ``_dependency_source_keys``
and ``__dependency_source`` variables to shorten the choices.

They correspond to the following options:

.. list-table:: dependency_source to __dependency_source
    :widths: 30 70
    :header-rows: 1

    * - __dependency_source 
      - dependency_source
    * - conda-forge
      - Prefer conda-forge over the default anaconda channel with pip fallback
    * - anaconda
      - Prefer default anaconda channel with pip fallback
    * - pip
      - Dependencies from pip only (no conda)


