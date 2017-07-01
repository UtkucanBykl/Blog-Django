from django.conf.urls import url

from . import views

app_name="articles"

urlpatterns=[
    #index
    url(r"^$", views.IndexView.as_view(), name="index"),
    #detail
    url(r'^(?P<id>[0-9]+)/$', views.detail, name="detail"),

    #software
    url(r"^software$", views.SoftwareArticle.as_view(), name="software"),
    #about
    url(r"^about$", views.AboutDetail.as_view(), name="about"),
    #like
    url(r'^(?P<id>[-\w]+)/like/$', views.like, name='like'),
    #search
    url(r"^search/$", views.search_titles,name="search"),
    #publish
    url(r'^(?P<id>[-\w]+)/publish/$', views.publish, name='publish'),

]