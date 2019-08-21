from django.shortcuts import render
from .api import load_tickers
from django.http import HttpResponse
import json


def query_tickers(request, article_uuid, amount):
    # Article_uuid could be saved for tracking
    tickers = load_tickers(amount)
    return HttpResponse(
        json.dumps({"newTickers": tickers}), content_type="application/json"
    )
