from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context = locals()
    template = 'index.html'
    return render(request,template,context)

@login_required
def userProfile(request):
    user = request.user
    context = {'user':user}
    template = 'menteelogin.html'
    return render(request,template,context)

@login_required
def userProfileNews(request):
    user = request.user
    context = {'user':user}
    template = 'news.html'
    return render(request,template,context)


@login_required
def userProfileMentor(request):
    user = request.user
    context = {'user':user}
    template = 'mentor.html'
    return render(request,template,context)

@login_required
def userProfileResources(request):
    user = request.user
    context = {'user':user}
    template = 'resources.html'
    return render(request,template,context)

@login_required
def userProfileFAQ(request):
    user = request.user
    context = {'user':user}
    template = 'FAQ.html'
    return render(request,template,context)

@login_required
def userProfileProfile(request):
    user = request.user
    context = {'user':user}
    template = 'profile.html'
    return render(request,template,context)

@login_required
def userProfileContent(request):
    user = request.user
    context = {'user':user}
    template = 'content.html'
    return render(request,template,context)
