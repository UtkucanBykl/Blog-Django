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
    url(r'/album/add/$', views.CreateArticle.as_view(), name="article-add"),
    #delete
    url(r'/article/(?P<pk>[0-9]+)/delete/$', views.DeleteArticle.as_view(), name="article-delete"),
    #comment

    url(r'^article/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^/(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name="profile"),

]