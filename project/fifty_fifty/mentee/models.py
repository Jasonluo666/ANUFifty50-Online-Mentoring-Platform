from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

GENDER = (
    ('M', 'male'),
    ('F', 'female'),
    ('O', 'other'),
    ('R', 'rather not say'),
)

# Create your models here.
class User_mentee(models.Model):
    gender = models.CharField(max_length=1, choices=GENDER)
