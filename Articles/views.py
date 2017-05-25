import json
import urllib
import urllib2
from django.db.models import Q
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from Articles.forms import CommentForm
from Articles.serializers import ArticleSerializer, CommentSerializer
from Blog import settings
from .models import Article, Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView,DeleteView
# Create your views here.
class IndexView(generic.ListView):
    template_name = "article/index.html"
    context_object_name = "all_articles"
    paginate_by=4
    def get_queryset(self):
        return Article.objects.filter(publish=True).order_by("-date")

class AboutDetail(generic.TemplateView):

    template_name = "article/about.html"



class SoftwareArticle(generic.ListView):
    context_object_name = "software"
    template_name = "article/softarticle.html"
    paginate_by=4
    def get_queryset(self):
        return Article.objects.filter(genre__startswith="software",publish=True).order_by("-date")


def detail(request, id):
    article = get_object_or_404(Article, id=id)
    if(request.user.is_authenticated):
        comments = Comment.objects.filter(Q(article__title__startswith=article.title))
    else:
        comments = Comment.objects.filter(Q(article__title__startswith=article.title), Q(publish=True))

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.urlencode(values)
            req = urllib2.Request(url, data)
            response = urllib2.urlopen(req)
            result = json.load(response)
            ''' End reCAPTCHA validation '''
            if result['success']:

                comment = form.save(commit=False)
                comment.article  = article
                comment.save()
                return redirect('articles:detail', id=article.id)
            else:
                error="Robot olmadigina emin misin ?"
                return render(request,"article/detail.html",{
                    "article":article,
                    "error":error,
                    "form":form,
                    "comments":comments
                })
    else:
        form = CommentForm()
    template = "article/detail.html"
    return render(request, template, {'form':form,
                                      "article":article,
                                      "comments":comments
                                      })

def publish(request, id):
    if (not request.user.is_authenticated):
        return redirect("articles:index")
    comment = get_object_or_404(Comment, id=id)
    if comment.publish:
        comment.publish = False
    else:
        comment.publish = True
    comment.save()
    return redirect("articles:detail", id=comment.article.id)

def like(request, id):
    article=get_object_or_404(Article, id=id)
    article.like+= 1
    article.save()
    return redirect('articles:detail', id=article.id)


def search_titles(request):
    if request.method == "POST":
        try:
            search_text = request.POST['search']
        except MultiValueDictKeyError:
            search_text = False
    else:
        search_text = ""
    articles = Article.objects.filter(title__icontains=search_text, publish=True) | \
             Article.objects.filter(body__icontains=search_text, publish=True)
    articles = articles.order_by("-date")
    if(not articles):
        error = "xss denemediyseniz aradiginiz sey yok"
        return render(request, "article/search.html", {"articles": articles, "search": search_text, "error":error})
    return render(request,"article/search.html", {"articles":articles, "search":search_text})




class CommentList(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer










