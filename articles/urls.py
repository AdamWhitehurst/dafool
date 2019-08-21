"""articles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from dafool.views import *
from comments.views import comment_create, comment_update, comment_delete
from tickers.views import query_tickers
from .views import article_view

urlpatterns = [
    path("<uuid>/", article_view),
    path("<article_uuid>/comment/create", comment_create),
    path("<article_uuid>/comment/update/<id>", comment_update),
    path("<article_uuid>/comment/delete/<id>", comment_delete),
    path("<article_uuid>/tickers/<int:amount>", query_tickers),
]
