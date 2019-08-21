import collections
import json
from random import randrange

featured_tag_slug = "10-promise"


def get_recent_article_array(recent_articles_count, can_be_featured=False):
    recent_articles = []

    while len(recent_articles) < recent_articles_count:
        new_recent_article = get_recent_article(can_be_featured)

        already_added = False
        for other_article in recent_articles:
            if new_recent_article.get("uuid") == other_article.get("uuid"):
                already_added = True
                break

        if not already_added:
            recent_articles.append(new_recent_article)

    return recent_articles


def get_recent_article(can_be_featured=False):
    # Get a random index
    article_list = list(uuid_to_article_dict.values())
    index = randrange(len(article_list))
    # Get article at random index
    recent_article = article_list[index]
    # If article cannot be the featured article
    if not can_be_featured:
        # Keep retrying until it isn't featured article
        while recent_article.get("uuid") == featured_article.get("uuid"):
            index = randrange(len(article_list))
            recent_article = article_list[index]
    # Return the recent article
    return recent_article


def get_article_by_uuid(uuid):
    if uuid in uuid_to_article_dict:
        return uuid_to_article_dict[uuid]
    return None


def check_featured_article(article):
    global featured_article
    if not featured_article:
        for tag in article.get("tags"):
            if tag.get("slug") == featured_tag_slug:
                featured_article = article


def get_featured_article():
    return featured_article


def set_new_featured_article(new_featured_tag_slug):
    global featured_article
    featured_article = None
    featured_tag_slug = new_featured_tag_slug
    for article in uuid_to_article_dict:
        # Check if article is featured Article's uuid
        check_featured_article(article)


def initialize_articles_api():
    # Intialize uuid-to-article dictionary
    u_t_a_d = {}
    # Load Contents from JSON
    content_json = open("content_api.json")
    formatted = json.load(content_json)
    articles = formatted["results"]
    # Fill uuid-to-article dictionary
    for article in articles:
        u_t_a_d[article.get("uuid")] = article
        # Check if article is featured Article's uuid
        check_featured_article(article)

    return u_t_a_d


featured_article = None
uuid_to_article_dict = initialize_articles_api()
