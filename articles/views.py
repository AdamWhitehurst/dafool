from django.shortcuts import render
from django.http import HttpResponse, Http404

from comments.models import Comment
from comments.forms import CommentForm
from comments.views import comment_create
from articles.api import get_article_by_uuid, get_similar_article_array
from tickers.api import get_ticker


def article_view(request, uuid):
    # Get the requested article
    target_article = get_article_by_uuid(uuid)

    # Raise a 404 if article uuid was not found
    if target_article is None:
        raise Http404

    # Get comments for the article
    comment_list = Comment.objects.filter(article_uuid=uuid)

    # Make a new Comment form
    initial_form_data = {"article_uuid": uuid}
    form = CommentForm(request.POST or None, initial=initial_form_data)
    if form.is_valid():
        created = comment_create(form)
        if created:
            print("Yeah")

    tickers = []
    # Query tickers
    for ticker in target_article.get("instruments"):
        tickers.append(get_ticker(ticker.get("company_name")))

    # Get read more links
    read_more_links = []
    collection_type = target_article.get("collection").get("slug")

    similar_articles = get_similar_article_array(
        collection_type=collection_type, amount=5
    )
    for article in similar_articles:
        link = {"headline": article.get("headline"), "uuid": article.get("uuid")}
        read_more_links.append(link)

    # Compose context
    context = {
        "article": target_article,
        "comment_list": comment_list,
        "form": form,
        "ticker_list": tickers,
        "read_more_links": read_more_links,
    }

    return render(request, "articles/article.html", context=context)
