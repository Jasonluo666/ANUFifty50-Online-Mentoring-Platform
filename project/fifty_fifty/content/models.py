import os
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver



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

@receiver(pre_delete, sender=Post)
@receiver(pre_delete, sender=Mentor)
@receiver(pre_delete, sender=Mentee)
@receiver(pre_delete, sender=Training)
def delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.docfile.delete(False)

