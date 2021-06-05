from scripts.fetch import fetchData
from scripts.process import processData
import pandas as pd
from scripts.data import Data


def getData(ticker, name):
    print(40*"=")
    print("WARNING: THIS COULD TAKE AROUND 3 MIN")
    print(40*"=")
    fetchData(ticker, name)
    processData(ticker, name)
    data = Data(ticker)
    data.load_data(pump_thresold=0.01)
    return data.df

if __name__ == '__main__':
    getData()
