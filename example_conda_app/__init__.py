"""Main entrypoint into our application's package."""

from __future__ import absolute_import
import pandas as pd

def main():
    """Load up some data into a DataFrame and print it out."""
    df = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'a', 'd']})
    print df.head()

# computes the version from git tag (managed by versioneer)
from example_conda_app._version import get_versions
__version__ = get_versions()['version']
del get_versions
