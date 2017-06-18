from django.contrib.sitemaps import Sitemap
from .models import Article

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Article.objects.filter(publish=True)

    def lastmod(self, obj):
        return obj.filter(publish=True)