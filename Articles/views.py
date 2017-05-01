import json
import urllib
import urllib2

from django.core.checks import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.cache import cache_page

from Articles.forms import CommentForm
from Blog import settings
from .models import Article, Comment
from django.shortcuts import render,redirect
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class IndexView(generic.ListView):
    template_name = "article/index.html"
    context_object_name = "all_articles"
    paginate_by=4
    def get_queryset(self):
        return Article.objects.order_by("-date")

class AboutDetail(generic.TemplateView):

    template_name = "article/about.html"

class DetailView(generic.DetailView):
    model=Article
    template_name = "article/detail.html"


class CreateArticle(generic.CreateView):
    model = Article
    fields = ["title","body","genre"]
    template_name = "article/article_form.html"

class DeleteArticle(generic.DeleteView):
    model = Article
    success_url = reverse_lazy("articles:index")

class SoftwareArticle(generic.ListView):
    context_object_name = "software"
    template_name = "article/softarticle.html"
    paginate_by=4
    def get_queryset(self):
        return Article.objects.filter(genre__startswith="software").order_by("-date")


def add_comment(request, id):
    article = get_object_or_404(Article, id=id)
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
                return redirect('articles:detail', pk=article.pk)
            else:
                messages.Error(request, 'Invalid reCAPTCHA. Please try again.')

    else:
        form = CommentForm()
    template="article/comment.html"
    return render(request, template, {'form': form})

def like(request,id):
    article=get_object_or_404(Article,id=id)
    article.like+=1
    article.save()
    return render(request,'article/detail.html',{'article':article})

def search_titles(request):
    if request.method=="POST":
        try:
            search_text = request.POST['search']
        except MultiValueDictKeyError:
            search_text = False
    else:
        search_text=""
    articles=Article.objects.filter(title__contains=search_text)
    return render(request,"article/search.html",{"articles":articles,"search":search_text})






