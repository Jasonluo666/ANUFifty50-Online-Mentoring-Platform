from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from content.models import Post, Mentee, Mentor, Training
from webcore.models import Profile, Xpairs
#from content

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
    template = 'mentor.html'
    return render(request,template)

@login_required
def userProfileResources(request):
    user = request.user
    context = {'user':user, 'post_list':Post.objects.all(), 'mentee_list':Mentee.objects.all(), 'mentor_list':Mentor.objects.all(), 'training_list':Training.objects.all()}
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
    context = {'user':user, 'mentee_list':Mentee.objects.all()}
    template = 'content.html'
    return render(request,template,context)

@login_required
def userProfileContact(request):
    user = request.user
    context = {'user':user}
    template = 'contact.html'
    return render(request,template,context)
