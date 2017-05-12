from django.contrib import admin
from django.db import models
from django_markdown.admin import MarkdownModelAdmin

from .models import Article, Comment
from markdownx.widgets import AdminMarkdownxWidget


# Register your models here.


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }
    list_display = ["title", "genre"]
    list_filter = ["genre"]
    search_fields = ["title"]

    class Meta:
        model = Article

admin.site.register(Article,MyModelAdmin)
admin.site.register(Comment)
