from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

import pandas as pd

def main():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'a', 'd']})
    print df.head()
