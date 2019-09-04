import collections
import json
from random import randrange

featured_tag_slug = "10-promise"


def get_recent_article_array(amount, can_be_featured=False):
    recent_articles = []

    while len(recent_articles) < amount:
        new_recent_article = get_random_article(can_be_featured=can_be_featured)

        already_added = check_if_in_collection(new_recent_article, recent_articles)

        if not already_added:
            recent_articles.append(new_recent_article)

    return recent_articles


def check_if_in_collection(article, article_collection):
    for other_article in article_collection:
        if article.get("uuid") == other_article.get("uuid"):
            return True
    return False


def get_random_article(article_list=None, can_be_featured=False):
    global all_articles

    if article_list is None:
        article_list = all_articles

    # Get a random index
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


def get_similar_article_array(collection_type, amount):
    similar_articles = []
    if collection_type in articles_by_collection_dict:
        while len(similar_articles) < amount:
            new_similar_article = get_random_article(
                article_list=articles_by_collection_dict[collection_type],
                can_be_featured=True,
            )

            already_added = check_if_in_collection(
                new_similar_article, similar_articles
            )

            if not already_added:
                similar_articles.append(new_similar_article)
    return similar_articles


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
    # Load Contents from JSON
    content_json = open("content_api.json")
    formatted = json.load(content_json)
    return formatted["results"]


def initialize_uuid_dict(articles_list):
    # Intialize uuid-to-article dictionary
    u_t_a_d = {}
    # Fill uuid-to-article dictionary
    for article in articles_list:
        u_t_a_d[article.get("uuid")] = article
        # Check if article is featured Article's uuid
        check_featured_article(article)

    return u_t_a_d


def initialize_collections_dict(articles_list):
    collection_types = {}
    for article in articles_list:
        collection = article.get("collection")
        c_type = None
        if collection:
            c_type = collection.get("slug")
        if c_type is not None:
            if c_type not in collection_types:
                collection_types[c_type] = []
            collection_types[c_type].append(article)

    return collection_types


featured_article = None
all_articles = initialize_articles_api()
uuid_to_article_dict = initialize_uuid_dict(all_articles)
articles_by_collection_dict = initialize_collections_dict(all_articles)
