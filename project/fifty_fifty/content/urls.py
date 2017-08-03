from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', list, name='list')
]
