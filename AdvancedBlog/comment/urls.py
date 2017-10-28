from django.conf.urls import url

from comment import views

app_name = "comment"

urlpatterns = [
    url(r'^$', views.PostComments, name="post_comment"),
    url(r'^send/(?P<slug>[\w-]+)$', views.SendComment, name="send_comment"),


]