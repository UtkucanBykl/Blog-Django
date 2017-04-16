from django.contrib import admin
from .models import Article, Comment


# Register your models here.

class PostAdmin(admin.ModelAdmin):

    list_display = ["title","genre"]
    list_filter = ["genre"]
    search_fields = ["title"]
    class Meta:
        model=Article


admin.site.register(Article,PostAdmin)
admin.site.register(Comment)