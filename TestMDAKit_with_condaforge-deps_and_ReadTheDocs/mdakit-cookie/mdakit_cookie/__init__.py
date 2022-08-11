"""
TestMDAKit_with_condaforge-deps_and_ReadTheDocs
Test MDAKit Project with dependencies using condaforge and ReadTheDocs
"""

# Add imports here
from .mdakit_cookie import canvas

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
