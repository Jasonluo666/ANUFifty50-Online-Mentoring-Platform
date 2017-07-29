from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone
from .models import Post, Mentor, Mentee
from django.http import HttpResponse

class PostList(ListView):
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    model = Post
    template_name = 'profile.html'


class MenteeList(ListView):
    model = Mentee
    template_name = '../webcore/templates/content.html'

