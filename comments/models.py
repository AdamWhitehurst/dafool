from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
import datetime

# from articles.models import Article


class Comment(models.Model):
    article_uuid = models.TextField(null=True)

    name = models.CharField(max_length=30)
    body = models.TextField(blank=False)
    post_date = models.DateField(default=datetime.datetime.now)
