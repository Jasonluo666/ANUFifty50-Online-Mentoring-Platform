from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django import forms
from .models import Profile

YEAR_OF_STUDY = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5+','5+'),
)

BACHELOR_DEGREE_PROGRAMME = (
    ('','-'),
    ('AACOM','Advanced Computing (Honours)'),
    ('AACRD','Advanced Computing (R&D) (Honours)'),
    ('BADAN','Applied Data Analytics'),
    ('HADAN','Applied Data Analytics (Honours)'),
    ('BBIOT','Biotechnology'),
    ('HBIOT','Biotechnology (Honours)'),
    ('AENGI','Engineering (Honours)'),
    ('AENRD','Engineering (R&D) (Honours)'),
    ('BENSU','Environment and Sustainability'),
    ('HENSU','Environment and Sustainability (Honours)'),
    ('AENSU','Environment and Sustainability Advanced (Honours)'),
    ('HENVS','Environemntal Studies'),
    ('BGENE','Genetics'),
    ('HGENE','Genetics (Honours)'),
    ('BHLTH','Health Science (Honours)'),
    ('BIT','Information Technology'),
    ('HIT','Information Technology (Honours)'),
    ('BMASC','Mathematical Sciences'),
    ('HMASC','Mathematical Sciences (Honours)'),
    ('BMEDS','Medical Science'),
    ('HMEDS/HMDSA','Medical Science (Honours)'),
    ('PHBSCIENCE', 'PhB / Bachelor of Philosophy (Honours) in Science'),
    ('APSYC','Psychology (Honours)'),
    ('BSC','Science'),
    ('HSC','Science (Honours)'),
    ('ASCAD','Science (Advanced) (Honours)'),
    ('BSPSY','Science (Psychology)'),
    ('HSPSY','Science (Psychology) (Honours)'),
    ('ASENG','Software Engineering (Honours)'),
    ('ESCIE','Diploma of Science'),
    ('ECOMP','Diploma of Computing'),
)


ROLES = (
    ('Mentee', 'Mentee'),
    ('Mentor', 'Mentor'),
)

GENDER = (
    ('', '-'), #error-checking st. "-" isn't a valid answer
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
    role = forms.ChoiceField(choices=ROLES, widget=forms.RadioSelect(attrs={'onclick': 'teetorCheck();'}), label='Would you like to register as a')
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    uniId = forms.CharField(max_length=100, label='University ID')
    study_year = forms.ChoiceField(choices=YEAR_OF_STUDY, label="Year of Study")
    degree_programme = forms.ChoiceField(choices=BACHELOR_DEGREE_PROGRAMME, label='Bachelor Degree Program 1')
    degree_programme_2 = forms.ChoiceField(choices=BACHELOR_DEGREE_PROGRAMME, required = False, label='Bachelor Degree Program 2 (if applicable, e.g. flexible double degree)')
    degree_major = forms.CharField(max_length=30, required = False, label='What is your degree major?')
    gender = forms.ChoiceField(choices=GENDER, label='What gender do you identify as?')
    mentor_gender = forms.ChoiceField(choices=MENTOR_GENDER, label='Would you prefer a mentee/mentor that is the same gender as you?')
    why_mentor = forms.CharField(max_length=150, required = False, widget=forms.Textarea, label='Why do you want to become a mentor?')
    why_div_equ_inc = forms.CharField(max_length=150, required = False, widget=forms.Textarea, label='Why do you think diversity, equity and inclusion in STEM are important?')
    mentee_number = forms.IntegerField(min_value = 1, max_value = 3, initial = 1, required = False, label='How many mentees would you like to have?')
    hear_about = forms.CharField(max_length=150, widget=forms.Textarea, required = False, label='How did you hear about this program?')

    def signup(self, request, user):

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']


        user.profile.role = self.cleaned_data['role']
        user.profile.uniId = self.cleaned_data['uniId']
        user.profile.study_year = self.cleaned_data['study_year']
        user.profile.degree_programme = self.cleaned_data['degree_programme']
        user.profile.degree_programme_2 = self.cleaned_data['degree_programme_2']
        user.profile.degree_major = self.cleaned_data['degree_major']
        user.profile.gender = self.cleaned_data['gender']
        user.profile.mentor_gender = self.cleaned_data['mentor_gender']
        user.profile.why_mentor = self.cleaned_data['why_mentor']
        user.profile.why_div_equ_inc = self.cleaned_data['why_div_equ_inc']
        user.profile.mentee_number = self.cleaned_data['mentee_number']
        user.profile.hear_about = self.cleaned_data['hear_about']

        user.profile.save()
        user.save()
