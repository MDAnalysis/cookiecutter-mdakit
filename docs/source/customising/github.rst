
Adding the project to GitHub
============================

The generated ``{repo_name}`` directory should be an initialised git repository.
We now need to connect it to GitHub:

#. `Create a new repository on GitHub <https://docs.github.com/en/get-started/quickstart/create-a-repo>`_ .
   **Do not** initialize the repo with a README, license, or any other files.
#. Push the local repository to GitHub.
   The `GitHub documentation <https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github#adding-a-local-repository-to-github-using-git>`_ should provide instructions for doing so, but in short:

   * Add the remote named ``origin`` with :code:`git remote add origin <URL>`
   * Push the local repository to the remote repository with :code:`git push -u origin main`
   * Verify files were pushed successfully by checking on GitHub


.. _github-features:

**GitHub features**

The ``.github/`` directory contains configuration files for useful features in 
GitHub, including:

* ``workflows/gh-ci.yaml`` for :ref:`running Continuous Integration <continuous-integration>`
  using `GitHub Actions <https://docs.github.com/en/actions>`_. Other GitHub 
  actions, e.g. for deployments, can be added to the ``workflows/`` directory.
* ``.github/ISSUE_TEMPLATE/`` and ``.github/PULL_REQUEST_TEMPLATE.md`` provide 
  templates that will be presented by GitHub to community members when making 
  Issues and Pull Requests on your project's repository. They will help guide 
  users/contributors to include all the relevant information, simplifying the 
  process for both you and them.

