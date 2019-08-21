import collections
import json
from random import randrange


def load_tickers(amount):
    return_tickers = []

    while len(return_tickers) < amount:
        new_ticker = get_ticker()

        already_added = False
        for other_ticker in return_tickers:
            if new_ticker.get(dict_name_field) == other_ticker.get(dict_name_field):
                already_added = True
                break

        if not already_added:
            return_tickers.append(new_ticker)

    return return_tickers


def get_ticker(name=None):
    # if no name specified, find random
    if name is None:
        # Get a random index
        index = randrange(len(tickers))
        # Get ticker at random index
        return tickers[index]
    # Else, try to return the named ticker
    elif name in ticker_name_dict:
        return ticker_name_dict[name]
    # Return none otherwise
    return None


def initialize_tickers_api():
    # Load Contents from JSON
    quotes_json = open("quotes_api.json", encoding="utf8")
    # Initialize list of tickers
    tickers = json.load(quotes_json)
    # Intialize dict from ticker name to ticker object
    ticker_name_dict = {}
    for ticker in tickers:
        ticker_name_dict[ticker.get(dict_name_field)] = ticker

    return tickers, ticker_name_dict


# The ticker object field that is used as key for ticker_name_dict
dict_name_field = "CompanyName"

tickers, ticker_name_dict = initialize_tickers_api()
