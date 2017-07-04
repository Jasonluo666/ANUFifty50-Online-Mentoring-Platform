from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostList.as_view(), name='post_list'),
]
