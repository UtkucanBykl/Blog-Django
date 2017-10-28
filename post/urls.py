from django.conf.urls import url

from post import views

app_name = "post"

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)$', views.PostDetailView, name="detail"),
    url(r'^like/(?P<slug>[\w-]+)$', views.LikePostView, name="like"),
    url(r'^dislike/(?P<slug>[\w-]+)$', views.DislikeView, name="dislike"),
    url(r'^post/$', views.allpost, name="allpost"),

]