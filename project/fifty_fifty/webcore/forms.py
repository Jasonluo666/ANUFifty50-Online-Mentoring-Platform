from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms
from .models import Profile

DEGREE_PROGRAMME = (
    ('Science', 'Science'),
    ('Technology', 'Technology'),
    ('Engineering','Engineering'),
    ('Mathematics', 'Mathematics')
)

DEGREE_MAJOR = (
    ('MAJOR1', 'MAJOR1'),
    ('MAJOR2', 'MAJOR2'),
    ('MAJOR3', 'MAJOR3'),
)

GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    ('Rather not say', 'Rather not say'),
)


MENTOR_GENDER = (
    ('Definitely', 'Definitely'),
    ('If possible', 'If possible'),
    ('Unconcerned', 'Unconcerned'),
)

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    uniId = forms.CharField(max_length=100, label='University ID')
    study_year = forms.IntegerField(min_value = 2000, max_value = 2017, label='Year of Study')
    degree_programme = forms.ChoiceField(choices=DEGREE_PROGRAMME, label='What degree program are you in?')
    degree_major = forms.ChoiceField(choices=DEGREE_MAJOR, label='What is your major/subject area in which you focus? Drop down options?')
    gender = forms.ChoiceField(choices=GENDER, label='What gender do you identify as?')
    mentor_gender = forms.ChoiceField(choices=MENTOR_GENDER, label='Would you prefer a mentee/mentor that is the same gender as you?')
    why_mentor = forms.CharField(max_length=150, required = False, widget=forms.Textarea, label='Why do you want to become a mentor?')
    why_div_equ_inc = forms.CharField(max_length=150, required = False, widget=forms.Textarea, label='Why do you think diversity, equity and inclusion in STEM are important?')
    mentee_number = forms.IntegerField(min_value = 1, max_value = 3, initial = 1, required = False, label='How many mentees would you like to have?')
    hear_about = forms.CharField(max_length=150, widget=forms.Textarea, required = False, label='How did you hear about this program?')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']


        user.profile.uniId = self.cleaned_data['uniId']
        user.profile.study_year = self.cleaned_data['study_year']
        user.profile.degree_programme = self.cleaned_data['degree_programme']
        user.profile.degree_major = self.cleaned_data['degree_major']
        user.profile.gender = self.cleaned_data['gender']
        user.profile.mentor_gender = self.cleaned_data['mentor_gender']
        user.profile.why_mentor = self.cleaned_data['why_mentor']
        user.profile.why_div_equ_inc = self.cleaned_data['why_div_equ_inc']
        user.profile.mentee_number = self.cleaned_data['mentee_number']
        user.profile.hear_about = self.cleaned_data['hear_about']

        user.profile.save()
        user.save()
