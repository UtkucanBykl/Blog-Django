from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from comment.forms import CommentForm
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