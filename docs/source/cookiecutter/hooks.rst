Hook scripts
============


pre_gen_project.py
------------------

This script is run after the user has entered values
for the prompt, but before the project is generated.

Two important things happen here, in different places:

#. Variables are substituted back into the cookiecutter.
   Because this relies on Jinja variable injection,
   it occurs in the docstring of the file.
#. Validation of the values. This occurs in the Python.
   The ``author_email``, ``repo_name``, ``package_name``,
   ``github_username``, ``github_host_account``, and
   ``ttemplate_analysis_class`` variables are validated
   against regular expressions.


post_gen_project.py
-------------------

This script is run after the project is generated.
It accomplishes the following steps:

* removes unnecessary files (e.g. the template analysis files, if no analysis class is specified)
* tries to initialize a git repository
* checkout a ``main`` branch
* adds an initial commit

