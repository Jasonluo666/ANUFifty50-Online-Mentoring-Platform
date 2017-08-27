from django.conf.urls import *
from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^list/$', list, name='list'),
    url(r'^admin/', include(admin.site.urls)),
]
