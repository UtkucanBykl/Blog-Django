from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
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

def AboutView(request):
    return render(request, "about.html")