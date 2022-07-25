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

"""

import re
import sys

REGEX_EMAIL = r'^[^@]+@[^@]+\.[^@]+$'
REGEX_ONLINE = r'^[_\-a-zA-Z][_\-a-zA-Z0-9]+$'
REGEX_MODULE = r'^[_a-zA-Z][_a-zA-Z0-9]+$'


def validate(regex: str, value: str, field: str):
    if not re.match(regex, value):
        print('ERROR: "{}" is not a valid {}!'.format(value, field))

        # exits with status 1 to indicate failure
        sys.exit(1)


if __name__ == "__main__":

    validate(REGEX_EMAIL, "{{ cookiecutter.author_email }}", "email")
    validate(REGEX_ONLINE, "{{ cookiecutter.repo_name }}", "repo name")
    validate(REGEX_ONLINE,
             "{{ cookiecutter.github_username }}", "GitHub username")
    validate(REGEX_ONLINE,
             "{{ cookiecutter.github_host_account }}", "GitHub account")
    validate(
        REGEX_MODULE,
        "{{ cookiecutter.package_name }}",
        "module name"
    )
