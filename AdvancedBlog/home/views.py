from django.contrib import messages
from django.core.mail import EmailMessage
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

# Create your views here.
from home.tasks import send_email
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

def ContactView(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        try:
            send_email.delay(name, message, email)
            messages.info(request, "Mail Yollandı")
        except:
            messages.error(request, "Mail Yollanamadı")
    return render(request, "contact.html")