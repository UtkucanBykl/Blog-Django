from django.conf.urls import url

from comment import views

app_name = "comment"

urlpatterns = [

    url(r'^send/(?P<slug>[\w-]+)$', views.SendComment, name="send_comment"),

]