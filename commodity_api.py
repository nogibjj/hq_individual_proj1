from fastapi import FastAPI
import uvicorn
from commodity import getrecord


app = FastAPI()


@app.get("/")
def root():
    """Returns default values when no input is given"""
    return getrecord()


@app.get("/get_price/{commodity_type}/{commodity_date}")
def search_return_price(commodity_type: str, commodity_date: str):
    """Returns commodity price based on commodity type and date"""
    result = getrecord(commodity_date,commodity_type)
    return result


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")