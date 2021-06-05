from scripts.fetch import fetchData
from scripts.process import processData


def getData(ticker, name):
    print(40*"=")
    print("WARNING: THIS COULD TAKE AROUND 3 MIN")
    print(40*"=")
    fetchData(ticker, name)
    processData(ticker, name)


if __name__ == '__main__':
    getData()
