import twint
import datetime as dt
from pathlib import Path

path_original = Path(__file__).resolve().parents[1]
path_data = (path_original / "../data/raw/").resolve()
path_data_processed = (path_original / "../data/processed/").resolve()

def getTweets(ticker, name):

    #look for tweets for each crypto
    tod = dt.datetime.now()
    d = dt.timedelta(days = 27)
    start_date = (tod-d).strftime("%Y-%m-%d")

    print(f"FETCHING TWITTER DATA FOR {name}...")
    c = twint.Config()
    c.Search = name
    c.Custom["tweet"] = ["id", "created_at","username","tweet", "likes_count"]
    c.Verified = True
    c.Lang = "en"
    if name == "Bitcoin":
        c.Min_replies = 200 # min replies
    else:
        c.Min_replies = 5
    c.Output = str(path_data) + f"/{ticker}_data_tweet.json"
    c.Since = start_date
    c.Store_json = True
    c.Hide_output = True

    tweets = twint.run.Search(c)
    print("FINISHED FETCHING TWITTER")
