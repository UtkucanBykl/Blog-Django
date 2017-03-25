from django.shortcuts import render
from django.http import HttpResponse

from .forms import CommentForm
from .models import Article,UserProfile, Comment
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.views.generic import View
from django.http import Http404
from django.shortcuts import render,get_object_or_404
from datetime import datetime
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
# Create your views here.
class IndexView(generic.ListView):
    template_name = "article/index.html"
    context_object_name = "all_articles"

    def get_queryset(self):
        return Article.objects.all().order_by('id')[:5]



class DetailView(generic.DetailView):
    model=Article
    template_name = "article/detail.html"

class CreateArticle(generic.CreateView):
    model = Article
    fields = ["title","body","genre","user"]
    user=UserProfile.pk
    template_name = "article/article_form.html"

class DeleteArticle(generic.DeleteView):
    model = Article
    success_url = reverse_lazy("articles:index")

def add_comment_to_post(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article/detail.html', pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'article/detail.html', {'form': form})

class ProfileView(generic.DetailView):
    model=UserProfile
    template_name = "article/profile.html"