"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from django.contrib.sitemaps.views import sitemap
from Articles.sitemaps import PostSitemap
from Articles.views import ArticleViewSet, CommentList
from django.contrib.sitemaps.views import sitemap

sitemaps = {
    'posts': PostSitemap,
}
router = routers.DefaultRouter()
router.register(r'article',ArticleViewSet)
router.register(r'comment',CommentList)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r"^", include("Articles.urls")),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^', include(router.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),

]

