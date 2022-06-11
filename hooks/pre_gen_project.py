"""
Pre Cookie Generation script(s)

If any error is raised, the cookie cutter creation fails and crashes
"""

import re
import sys

def validate(regex: str, value: str, field: str):
    if not re.match(regex, value):
        print('ERROR: "{}" is not a valid {}!'.format(value, field))

        # exits with status 1 to indicate failure
        sys.exit(1)


if __name__ == "__main__":
    REGEX_EMAIL = r'^[^@]+@[^@]+\.[^@]+$'
    REGEX_MODULE = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

    validate(REGEX_EMAIL, "{{ cookiecutter.author_email }}", "email")
    validate(REGEX_MODULE, "{{ cookiecutter.repo_name }}", "repo name")
    validate(
        REGEX_MODULE,
        "{{ cookiecutter.first_module_name }}",
        "module name"
    )
