"""
Some ideas are taken from the following sources:

See this thread about unique problems with dask and data formatting:
  

"""

import pandas as pd
import dask.dataframe as dd

# dtype={'streams': 'float64'}

def pandas_load_books(location="datasets/books.csv"):
    """Load the books dataset into a pandas dataframe

    Assumes the dataset is in the datasets folder in the root of the project
    """
    return pd.read_csv(location)


def pandas_print_books(location="datasets/books.csv", record_number=0):
    """Display the books dataset

    print and returns a single email record from the books dataset
    """

    df = pd.read_csv(location, error_bad_lines=False)
    record = df["title"][record_number]
    print(record)
    return record


def dask_query_books(location="datasets/books.csv"):
    """Query the books dataset

    Assumes the dataset is in the datasets folder in the root of the project
    """

    ddf = dd.read_csv(location, blocksize=None, error_bad_lines=False)
    return ddf
