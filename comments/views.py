from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, HttpResponseRedirect
from .forms import CommentForm
from .models import Comment


def comment_list(request, article_uuid):
    queryset = Comment.objects.filter(article_uuid=article_uuid)
    context = {"object_list": queryset}
    return context


def comment_create(request, article_uuid):
    form = CommentForm(request.POST or None)
    if form.is_valid():
        article_uuid = form.cleaned_data.get("article_uuid")
        name = form.cleaned_data.get("name")
        body = form.cleaned_data.get("body")
        new_comment, created = Comment.objects.get_or_create(
            article_uuid=article_uuid, name=name, body=body
        )
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def comment_update(request, article_uuid, id):
    obj = get_object_or_404(Comment, id=id)
    form = CommentForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {"form": form}
    return context


def comment_delete(request, article_uuid, id):
    obj = get_object_or_404(Comment, id=id)
    obj.delete()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
