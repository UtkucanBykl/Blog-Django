# -*- coding: utf-8 -*-

import json

from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from comment.forms import CommentForm
from post.models import Post


def IndexView(request):
    posts = Post.objects.filter(status=True)

    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, "index.html", {"posts":posts})


def PostDetailView(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm()
    return render(request, "post_detail.html", {"post":post,"form":form})

def LikePostView(request, slug):
    if (request.session.has_key(slug+"like")):
        messages.error(request, "Daha önce oy verdin.")
        return redirect("post:detail", slug=slug)
    post = get_object_or_404(Post, slug=slug)
    request.session[slug+"like"] = True
    post.like_post()
    return redirect("post:detail", slug=slug)


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
