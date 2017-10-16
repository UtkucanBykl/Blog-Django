from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify


class Post(models.Model):

    user = models.ForeignKey("auth.User", related_name="posts")
    title = models.CharField(max_length=140)
    content = models.TextField()
    body = models.CharField(max_length=140)
    image = models.ImageField()
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey("Category", related_name="posts")
    like = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, max_length=60, editable=False)

    def __str__(self):
        return self.title


    def change_status(self):
        if self.status:
            self.status = False
            self.save()
        else:
            self.status = True
            self.save()

    def like_post(self):
        self.like += 1
        self.save()

    def disslike_post(self):
        self.like -= 1
        self.save()

class Category(models.Model):

    category_name = models.CharField(max_length=40)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name




@receiver(post_save, sender=Post)
def update_slug(sender, **kwargs):
    if kwargs["instance"].title != kwargs["instance"].slug:
        slug = slugify(kwargs['instance'].title.replace('ı', 'i'))
        Post.objects.filter(title=kwargs['instance'].title).update(slug=slug)