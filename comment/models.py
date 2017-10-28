from django.db import models

# Create your models here.

class Comment(models.Model):

    post = models.ForeignKey("post.Post", related_name="comments")
    username = models.CharField(max_length=40)
    comment = models.TextField(max_length=140)
    publish = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

    def publish_comment(self):
        if not self.publish:
            self.publish = True
            self.save()
