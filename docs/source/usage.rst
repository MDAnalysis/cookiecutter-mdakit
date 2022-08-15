Using the template
==================

Getting up and running requires a short process.

You will need the following:
    * Python 3.8+
    * The `cookiecutter`_ tool installed
    * A GitHub account


#. Use the cookiecutter to create a new project
------------------------------------------------

An example of using the cookiecutter is illustrated below.
The first line is the prompt, i.e. the actual
command to use. It is followed by all the prompts you can expect,
and some example answers.

.. literalinclude:: generated/cookiecutter_cli.log
    :language: bash
    :linenos:


This generates the output skeleton:

.. literalinclude:: generated/cookie_tree.txt

We will go more into these files in the rest of this
tutorial, as well as other sections in this documentation.

#. Add the project to GitHub
----------------------------

The generated repository should be an initialised git repository.
We now need to connect it to GitHub.


.. _cookiecutter: https://github.com/audreyr/cookiecutter
