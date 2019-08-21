from django.http import HttpResponse, Http404
from django.shortcuts import render
from articles.api import get_recent_article_array, get_featured_article


def home_view(request):
    recent_articles = get_recent_article_array(3)
    featured_article = get_featured_article()

    context = {"row_articles": recent_articles, "featured_article": featured_article}

    return render(request, "home.html", context=context)

