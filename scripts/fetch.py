#utilities
import os
from pathlib import Path

#project modules
import scripts.fetchScripts.getCryptodata as cryptoRaw
import scripts.fetchScripts.twitterdata as twitterRaw
import scripts.fetchScripts.pytrendFetch as pytrendRaw

path_original = Path(__file__).resolve().parents[1]
path_data_origin = (path_original / "./data/").resolve()
path_data = (path_original / "./data/raw/").resolve()
path_data_processed = (path_original / "./data/processed/").resolve()

def fetchData(ticker, name):
    #creates data directory if it does not exists
    if not os.path.isdir(str(path_data_origin)):
        os.mkdir(str(path_data))
        os.mkdir(str(path_data))


    cryptoRaw.getRawCrypto(ticker, name)
    twitterRaw.getTweets(ticker, name)
    pytrendRaw.addPytrend(ticker, name)



if __name__ == '__main__':
    fetchData()
