.. _customising-label:

Preparing and customising your project
######################################
Running the cookiecutter provides you with a skeleton for a Python package, 
including configuration files for several optional tools.  All generated files 
live in a the ``{repo_name}`` directory.

The next steps are to add your code, corresponding tests and documentation, 
and complete any extra steps to get optional tools running (e.g. linking to 
external services). The sections below provide more detail on these steps. 
Generated file will be discussed as the become relevant; see 
:ref:`files-label` for an overview of all the generated files.

.. toctree::
   :maxdepth: 1
   
   customising/github
   customising/code
   customising/tests
   customising/documentation
   customising/packaging


In addition to code and configuration files, the cookiecutter template 
includes several ready-to-go human-readable files intended to provide 
information to your users, contributors, or general community. Make sure to 
read each though and see that it matches your vision for your project, or 
ammend appropriately:

.. _general-info:

* **License:** Your code needs to be clearly licensed so that users know if 
  they can (legally) use it. The cookiecutter will apply the **GPLv2** 
  license by default, included in the ``LICENSE`` file. If you decide to use a
  different license (see `ChooseALicense <https://choosealicense.com/>`_), also 
  update the copyright infromation in ``README.md``.

* **README:** ``README.md`` is the introductory explanation to you project; it
  will be rendered on your GitHub repo's home page. It has been pre-filled with 
  some basic information, including your description and several badges that 
  provide at-a-glance information to users on current version, test status, and more.

.. _community-resources:

**Community resources**

* ``CODE_OF_CONDUCT.md`` outlines rules for behaviour for those in your community.
* ``CONTRIBUTING.md`` provides information and instructions for those who want to contribute.



Add your package to the MDAKit Registry!
========================================
The cookiecutter-generated template already ticks off most of the requirements
for registering your MDAKit on the `MDAKit Registry <https://mdakits.mdanalysis.org/>`_!

Once you've added your code, tests, and added the package to GitHub, you should
be ready to start the `registration process <https://mdakits.mdanalysis.org/addingakit.html>`_
(though it is recommended you continue to develop your package beyond these 
basic requirements).

.. _documenting-changes:

Documenting changes going forward
=================================
An initial ``AUTHORS.md`` (pre-populated with your name)  and tempate 
``CHANGELOG.md``  are also generated. As you go forward and develop your code, 
**update these files to track all contributors and important changes to your 
project**. Instructions are provided within each file suggesting the appropriate
format to use.

