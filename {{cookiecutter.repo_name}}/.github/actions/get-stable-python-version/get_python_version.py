#!/usr/bin/env python3

# MIT License

# Copyright (c) 2022 MDAnalysis Development Team

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


"""
Script to grab the latest N version of Python.
This is very helpful for CI purposes.
Note that only final releases are considered.

Example usage, when 3.10 is the latest active release, and 3.11 is in beta:

$ ./get_python_version.py
3.10
$ ./get_python_version.py --field major
3
$ ./get_python_version.py --field micro
3.10.6
$ ./get_python_version.py --field minor --last-n-version 1
3.9
$ ./get_python_version.py --field minor --last-n-version 2
3.8
$ ./get_python_version.py --field micro --last-n-version 2
3.10.4

"""


import argparse
import urllib.request
import json
from typing import NamedTuple, List, Tuple

FIELD_CHOICES = ["major", "minor", "micro"]

parser = argparse.ArgumentParser(
    description="Get the last n Python versions",
)
parser.add_argument(
    "--last-n-version",
    type=int,
    help=(
        "The version to check. 0 returns the latest release; "
        "1 returns the one before that"
    ),
    default=0,
)
parser.add_argument(
    "--field",
    choices=FIELD_CHOICES,
    help="Field to select last-n-version on",
    default="minor",
)


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int

    @classmethod
    def from_str(cls, version: str):
        releaselevel = "final"
        serial = 0
        if "-" in version:
            version, suffix = version.split("-")
            releaselevel, serial = suffix.split(".")
            serial = int(serial)

        major, minor, micro = map(int, version.split("."))
        return cls(
            major=major,
            minor=minor,
            micro=micro,
            releaselevel=releaselevel,
            serial=serial
        )


def get_release_versions(
    only_final_releases: bool = True
) -> List[VersionInfo]:
    MANIFEST_URL = 'https://raw.githubusercontent.com/actions/python-versions/main/versions-manifest.json'

    with urllib.request.urlopen(MANIFEST_URL) as response:
        content = response.read().decode('utf-8')

    version_dicts = json.loads(content)
    all_versions = [VersionInfo.from_str(v["version"]) for v in version_dicts]
    if only_final_releases:
        all_versions = [v for v in all_versions if v.releaselevel == "final"]
    return sorted(all_versions, reverse=True)


def return_python_version(
    last_n_version: int,
    field: str = "minor",
) -> Tuple[int, ...]:
    all_versions = get_release_versions(only_final_releases=True)
    field_index = FIELD_CHOICES.index(field)

    unique_versions = {v[:field_index + 1] for v in all_versions}
    sorted_unique = sorted(unique_versions, reverse=True)
    if last_n_version >= len(sorted_unique):
        return sorted_unique[-1]
    return sorted_unique[last_n_version]


if __name__ == "__main__":
    args = parser.parse_args()
    version = return_python_version(args.last_n_version, args.field)
    print(".".join(map(str, version)))
