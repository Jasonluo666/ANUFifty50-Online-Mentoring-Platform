import os
from django.db import models
from django.utils import timezone



class Post(models.Model):
    title = models.CharField(max_length=200)
    docfile = models.FileField(upload_to='news/', null=True)

    def __str__(self):
        return self.title

class Mentor(models.Model):
    title = models.CharField(max_length=200)
    docfile = models.FileField(upload_to='mentor/', null=True)

    def __str__(self):
        return self.title

class Mentee(models.Model):
    title = models.CharField(max_length=200)
    docfile = models.FileField(upload_to='mentee/', null=True)

    def __str__(self):
        return self.title

class Training(models.Model):
    title = models.CharField(max_length=200)
    docfile = models.FileField(upload_to='training/', null=True)
    
    def __str__(self):
        return self.title
