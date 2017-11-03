# -*- coding: utf-8 -*-

import json

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from comment.forms import CommentForm
from post.models import Post





def PostDetailView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()
    return render(request, "post_detail.html", {"post":post,"form":form})


def LikePostView(request, slug):
    response = {}
    if (request.session.has_key(slug+"like")):
        response["error"] = True
        response["text"] = "Daha Önce Oy kullanılmış"
        data = json.dumps(response)
        return HttpResponse(data)
    post = get_object_or_404(Post, slug=slug)
    request.session[slug+"like"] = True
    post.like_post()
    response["error"] = False
    response["text"] = "Oyunuz Kaydedildi"
    data = json.dumps(response)
    return HttpResponse(data)


def DislikeView(request, slug):
    if (request.session.has_key(slug+"dislike")):
        messages.error(request, "Daha önce oy verdin.")
        return redirect("post:detail", slug=slug)
    post = get_object_or_404(Post, slug=slug)
    request.session[slug+"dislike"] = True
    post.disslike_post()
    return redirect("post:detail", slug=slug)



def allpost(request):
    if request.method == 'POST':
        results = []
        change = request.POST.get("search")
        posts = Post.objects.filter(title__icontains=change)[:3]
        for post in posts:
            post_json = {}

            post_json['title'] = post.title
            post_json["content"] = post.content
            post_json["slug"] = post.slug

            results.append(post_json)
    data = json.dumps(results)
    return HttpResponse(data)

def deneme(request):
    if request.method == "POST":
        post_json = {}
        slug = request.POST.get("post")
        post = get_object_or_404(Post, slug=slug)
        like_count = post.like
        post_json["like"] = like_count
        data = json.dumps(post_json)
        return HttpResponse(data)