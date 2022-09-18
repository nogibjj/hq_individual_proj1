import dask.dataframe as dd


def dask_query_commodity(location="datasets/commodity_futures.csv"):
    """Query the commodity_futures dataset. 
       Assumes the dataset is in the datasets folder in the root of the project
    """

    ddf = dd.read_csv(location, blocksize=None)
    return ddf