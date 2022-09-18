from commodity_dask import dask_query_commodity


def getrecord(commodity_date = '2000-02-02', commodity_type = 'SOYBEANS'):
    """Return records from the commodity_futures dataset based on commodity type and date.
    By default, the function will return the commodity price for SOYBEANS on 2000-02-02.
    """
    ddf = dask_query_commodity()
    result = ddf[(ddf.Date == commodity_date)][commodity_type].compute()
    return f'The Price of {commodity_type} on {commodity_date} is ${list(result)[0]}.'
    