"""
TestMDAKit_with_host_MDAnalysis_anaconda-deps_and_no-ReadTheDocs
Test MDAKit Project with dependencies using anaconda and no ReadTheDocs
"""

# Add imports here

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
