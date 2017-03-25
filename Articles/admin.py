from django.contrib import admin
from .models import Article,UserProfile,Comment
# Register your models here.

admin.site.register(Article)
admin.site.register(UserProfile)
admin.site.register(Comment)