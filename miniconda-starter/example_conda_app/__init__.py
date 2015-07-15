import pandas as pd

def main():
    df = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'a', 'd']})
    print df.head()
