import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from comment.forms import CommentForm
from comment.models import Comment
from post.models import Post


def SendComment(request, slug):
    if request.method == "POST":
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.post = post
            com.save()
            return redirect("post:detail", slug=slug)
    return redirect("post:index")


def PostComments(request):
    if request.method == "POST":
        post_name = request.POST.get("post")
        if request.user.is_staff:
            comments = Comment.objects.filter(post__slug=post_name)
        else:
            comments = Comment.objects.filter(post__slug=post_name, publish=True)
        results = []
        for c in comments:
            c_json = {}
            c_json["username"] = c.username
            c_json["comment"] = c.comment
            results.append(c_json)
    data = json.dumps(results)
    return HttpResponse(data)
