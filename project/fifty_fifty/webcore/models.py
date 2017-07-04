from django.db import models
from django.db.models.fields import IntegerField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

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



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uniId = models.CharField(max_length=100)
    study_year = models.IntegerField(null = True, validators=[MinValueValidator(2000), MaxValueValidator(2017)])
    degree_programme = models.CharField(max_length=50, null = True ,choices=DEGREE_PROGRAMME)
    degree_major = models.CharField(max_length=50, null = True ,choices=DEGREE_MAJOR)
    gender = models.CharField(max_length=15, null = True ,choices=GENDER)
    mentor_gender = models.CharField(max_length=15, null = True ,choices=MENTOR_GENDER)
    why_mentor = models.CharField(max_length=150, null = True)
    why_div_equ_inc = models.CharField(max_length=150, null = True)
    mentee_number = models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(3)])
    hear_about = models.CharField(max_length=150, null = True)

    def __str__(self):
       return 'University ID ' + str(self.uniId)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
