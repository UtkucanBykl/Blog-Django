from __future__ import unicode_literals


from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
from django.db.models import Model
import datetime


class Article(models.Model):
    title=models.CharField(max_length=25,unique=True)
    body=models.CharField(max_length=140,unique=True)
    content=models.TextField()
    like=models.IntegerField(default=0)
    genre=models.CharField(max_length=10)
    date=models.DateTimeField(auto_now_add=True)
    publish=models.BooleanField(default=False)
    def get_absolute_url(self):

        return reverse("article:detail",kwargs={"pk":self.pk})

    def __unicode__(self):
        return self.title

    class Meta:
        ordering=["-date"]


class Comment(models.Model):
    name=models.CharField(max_length=25)
    date=models.DateTimeField(auto_now_add=True)
    comment=models.TextField(max_length=140)
    publish=models.BooleanField(default=False)
    article=models.ForeignKey('Articles.Article',related_name="comments",on_delete=models.CASCADE)

    def get_absolute_url(self):

        return reverse("comment:detail",kwargs={"pk":self.pk})

    def __unicode__(self):
        return self.comment

    class Meta:
        ordering = ['-date']



