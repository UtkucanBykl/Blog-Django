from django.contrib import admin
from django.db import models

from .models import Article, Comment
from pagedown.widgets import AdminPagedownWidget


# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ["title","genre"]
    list_filter = ["genre"]
    search_fields = ["title"]
    class Meta:
        model=Article




class AlbumAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }


admin.site.register(Article,AlbumAdmin)
admin.site.register(Comment)