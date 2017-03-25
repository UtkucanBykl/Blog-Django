from __future__ import unicode_literals

import datetime
from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models import Model


class Article(models.Model):
    title=models.CharField(max_length=25)
    body=models.TextField(max_length=250)
    genre=models.CharField(max_length=10)

    #user key
    user=models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse("article:detail",kwargs={"pk":self.pk})

    def __str__(self):
        return self.title+"-"+self.body

class UserProfile(models.Model):
    user=models.OneToOneField(User)

    avatar = models.ImageField()

    def __str__(self):
        return self.user.username+"-"+str(self.user.pk)

class Comment(models.Model):
    article=models.ForeignKey("Article",on_delete=models.CASCADE)
    name=models.CharField(max_length=25)
    lastname=models.CharField(max_length=30)
    text=models.TextField(max_length=140)
    date=models.DateTimeField()

    def __str__(self):
        return self.comment