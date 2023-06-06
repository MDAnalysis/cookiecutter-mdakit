"""
TestMDAKit_with_anaconda-deps_and_ReadTheDocs
Test MDAKit Project with dependencies using anaconda and ReadTheDocs
"""

# Add imports here

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions