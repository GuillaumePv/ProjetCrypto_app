from pytrends.request import TrendReq
from pytrends import dailydata
from datetime import date
import datetime as dt
import pandas as pd
import numpy as np
from pathlib import Path

path_original = Path(__file__).resolve().parents[1]
path_data = (path_original / "../data/raw/").resolve()
path_data_processed = (path_original / "../data/processed/").resolve()

def addPytrend(ticker, name):

    print("FETCHING TRENDS...")

    pytrends = TrendReq(hl='en-US', tz=360)

    tod = dt.datetime.now()
    tmonth = int(tod.strftime("%-m"))
    tyear = int(tod.strftime("%Y"))
    lyear = tyear
    if tmonth > 1:
        lmonth = tmonth - 1
    else:
        lmonth = 12
        lyear = tyear - 1

    dfTrend = dailydata.get_daily_data(name, lyear, lmonth, tyear, tmonth, verbose=False)
    dfTrend = dfTrend[[f'{name}_unscaled', f'{name}_monthly']]
    dfTrend.rename(columns = {f'{name}_unscaled':f'{name}_pytrend_unscaled', f'{name}_monthly':f'{name}_pytrend_monthly'}, inplace = True)
    dfTrend.to_csv(str(path_data) + f'/{ticker}_data_trend.csv')

if __name__ == '__main__':
    addPytrend()
