Using the template
==================

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
    :linenos:


This generates the output skeleton:

.. literalinclude:: generated/cookie_tree.txt

We will go more into these files in the rest of this
tutorial, as well as other sections in this documentation.

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



.. _cookiecutter: https://github.com/audreyr/cookiecutter
.. _`Create a new repository on GitHub`: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository