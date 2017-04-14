from __future__ import unicode_literals

import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.utils import timezone

# Create your models here.
from django.db.models import Model
import datetime


class Article(models.Model):
    title=models.CharField(max_length=25)
    body=models.CharField(max_length=140)
    content=models.TextField()
    genre=models.CharField(max_length=10)
    date=models.DateTimeField(default=datetime.datetime.now())
    publish=models.BooleanField(default=False)
    def get_absolute_url(self):

        return reverse("article:detail",kwargs={"pk":self.pk})

    def __str__(self):
        return self.title+"-"+self.body