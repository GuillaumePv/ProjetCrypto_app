#utilities
import os
import sys
from pathlib import Path
import json
from pathlib import Path

#data science librairies
import numpy as np
import pandas as pd

path_original = Path(__file__).resolve().parents[1]
path_data = (path_original / "../data/raw/").resolve()
path_data_processed = (path_original / "../data/processed/").resolve()

'''
data_path = "../data/raw/"
clean_data_path = "../data/processed/"
eth_file = data_path+"ETH_raw.csv"
btc_file = data_path+"BTC_raw.csv"
eos_file = data_path+'EOS_raw.csv'

file_list = [eth_file,btc_file,eos_file]
list_ticker = ['ETH','BTC','EOS']

# faire une classe pour générer les données => folder 'data'
#create a function
def processPricedata(file,ticker):
    df = pd.read_csv(file)
    df['date'] = pd.to_datetime(df['Date'],unit="s")
    #df_btc.index = df_btc['Date']
    del df['Date']
    del df['Ignore']
    # del df_btc['CloseTime']
    df.to_csv(clean_data_path+ticker+'_Price_clean.csv')
    return df

list_df = []
for i in range(len(file_list)):
    list_df.append(processPricedata(file_list[i],list_ticker[i]))
'''

##############################
## Merge DB price & Twitter ##
##############################

def mergeBinance(ticker, name):
    print("MERGING BINANCE AND TWEETS TOGETHER...")



    df_data = pd.read_csv(str(path_data) + f"/{ticker}_data.csv")



    clean_data_path = str(path_data_processed) + "/"

    ## Path
    tweet = str(path_data_processed) + f"/{ticker}_tweet_clean.csv"

    df = pd.read_csv(tweet)
    df = df.sort_values('date')


    df_data.rename(columns = {'Date':'date'}, inplace = True)
    df_data['date'] = pd.to_datetime(df_data['date'], unit = 's')
    df_data['date'] = pd.to_datetime(df_data['date'])
    df['date'] = pd.to_datetime(df['date'])

    df_outer = df_data.merge(df, on=['date'], how='left') #beug ici
    df_outer.to_csv(clean_data_path+ticker+'_finaldb.csv', index=False)

    #Adding the pytrend data
    dfTrend = pd.read_csv(str(path_data) + f'/{ticker}_data_trend.csv')
    df = pd.read_csv(clean_data_path+ticker+'_finaldb.csv')
    df = df.merge(dfTrend, on=['date'], how='left')
    df = df[df['Close'] > 0]
    df.to_csv(clean_data_path+ticker+'_finaldb.csv', index=False)
