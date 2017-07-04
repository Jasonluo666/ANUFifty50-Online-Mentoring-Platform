from django.conf.urls import url
from . import views

app_name = 'mentee'

urlpatterns = [

    # /users/signup:url to take the input from the user
    url(r'^mentee_signup$', views.signup, name='mentee_signup'),
]
