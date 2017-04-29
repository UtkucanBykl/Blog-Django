from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name="articles"

urlpatterns=[
    #index
    url(r"^$", views.IndexView.as_view(), name="index"),
    #detail
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    #add
    url(r'^album/add/$', views.CreateArticle.as_view(), name="article-add"),
    #delete
    url(r'^article/(?P<pk>[0-9]+)/delete/$', views.DeleteArticle.as_view(), name="article-delete"),
    #software
    url(r"^software$", views.SoftwareArticle.as_view(), name="software"),
    #about
    url(r"^about$", views.AboutDetail.as_view(), name="about"),
    #comment
    url(r'^(?P<id>[-\w]+)/comment/$', views.add_comment, name='add_comment'),

]