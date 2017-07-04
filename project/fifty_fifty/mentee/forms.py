from django import forms

GENDER = (
    ('M', 'male'),
    ('F', 'female'),
    ('O', 'other'),
    ('R', 'rather not say'),
)

class User_menteeform(forms.Form):

    gender = forms.ChoiceField(choices=GENDER, required=True )
    
