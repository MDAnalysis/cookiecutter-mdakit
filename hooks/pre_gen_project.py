"""
Pre Cookie Generation script(s)

If any error is raised, the cookie cutter creation fails and crashes



=== VARIABLE INJECTION ===
This next section uses the fact that the script is rendered with Jinja
prior to execution to inject values into the template.

It checks to see if the `github_host_account` is the default value,
i.e. the instructional help text. If so, it replaces the value with
`github_username`.

Then it adds a `github_url` variable for easier use with CI, etc.

{{ cookiecutter.update({"github_host_account": cookiecutter.github_host_account | trim }) }}

{% if (not cookiecutter.github_host_account or "organization account" in cookiecutter.github_host_account) %}
    {{ cookiecutter.update({ "github_host_account": cookiecutter.github_username }) }}
{% else %}
    {{ cookiecutter.update({ "github_host_account": cookiecutter.github_host_account }) }}
{% endif %}

{{ cookiecutter.update({"github_url": [cookiecutter.github_host_account, cookiecutter.repo_name]|join("/") }) }}


--- ANALYSIS ---

Set `template_analysis_class` to "" if default value is passed.

{{ cookiecutter.update({"template_analysis_class": cookiecutter.template_analysis_class | trim }) }}

{% if "Press Enter to skip" in cookiecutter.template_analysis_class %}
    {{ cookiecutter.update({ "template_analysis_class": "" }) }}
{% endif %}


=== LICENSE ===

{{ cookiecutter.update({"open_source_license": 'GNU Public License v2+'}) }}

"""

import re
import sys

REGEX_EMAIL = r'^[^@]+@[^@]+\.[^@]+$'
REGEX_URL_COMPATIBLE = r'^[_\-a-zA-Z][_\-a-zA-Z0-9]+$'
REGEX_PYTHON_COMPATIBLE = r'^[_a-zA-Z][_a-zA-Z0-9]+$'


def validate(regex: str, value: str, field: str, allow_empty: bool = False):
    if allow_empty and not value:
        return
    if not re.match(regex, value):
        print('ERROR: "{}" is not a valid {}!'.format(value, field))

        # exits with status 1 to indicate failure
        sys.exit(1)


if __name__ == "__main__":

    validate(REGEX_EMAIL, "{{ cookiecutter.author_email }}", "email")
    validate(REGEX_URL_COMPATIBLE, "{{ cookiecutter.repo_name }}", "repo name")
    validate(REGEX_URL_COMPATIBLE,
             "{{ cookiecutter.github_username }}", "GitHub username")
    validate(REGEX_URL_COMPATIBLE,
             "{{ cookiecutter.github_host_account }}", "GitHub account")
    validate(
        REGEX_PYTHON_COMPATIBLE,
        "{{ cookiecutter.package_name }}",
        "module name"
    )
    validate(
        REGEX_PYTHON_COMPATIBLE,
        "{{ cookiecutter.template_analysis_class }}",
        "analysis class name",
        allow_empty=True
    )
