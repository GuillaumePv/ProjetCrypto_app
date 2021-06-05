import scripts.processScripts.tweetProcess as tweetProcess
import scripts.processScripts.mergerProcess as merger
import scripts.processScripts.indicatorProcess as indicators
import scripts.processScripts.yahooProcess as yahoo

def processData(ticker, name):
    tweetProcess.cleanTweets(ticker, name)
    merger.mergeBinance(ticker, name)
    indicators.addIndicators(ticker, name)
    yahoo.getData(ticker, name)


if __name__ == '__main__':
    processData(ticker, name)
