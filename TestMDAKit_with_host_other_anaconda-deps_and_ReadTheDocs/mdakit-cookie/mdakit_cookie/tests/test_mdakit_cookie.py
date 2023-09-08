"""
Unit and regression test for the mdakit_cookie package.
"""

# Import package, test suite, and other packages as needed
import mdakit_cookie
import pytest
import sys


def test_mdakit_cookie_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "mdakit_cookie" in sys.modules


def test_mdanalysis_logo_length(mdanalysis_logo_text):
    """Example test using a fixture defined in conftest.py"""
    logo_lines = mdanalysis_logo_text.split("\n")
    assert len(logo_lines) == 46, "Logo file does not have 46 lines!"
