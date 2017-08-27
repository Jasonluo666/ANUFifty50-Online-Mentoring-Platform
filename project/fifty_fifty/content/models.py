import os
from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.db.models.signals import post_delete
from django.dispatch.dispatcher import receiver
from django.core.urlresolvers import reverse



class Post(models.Model):
    title = models.CharField(max_length=255,null=True)
    slug = models.SlugField(unique=True, max_length=255,null=True)
    description = models.CharField(max_length=255,null=True)
    content = models.TextField(null=True)
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return u'%s' % self.title

    ##def get_absolute_url(self):
      ##  return reverse('webcore.views.post', args=[self.slug])


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


#Delete content from folder
@receiver(post_delete, sender=Mentor)
@receiver(post_delete, sender=Mentee)
@receiver(post_delete, sender=Training)
def delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.docfile.delete(False)

#Edit content from folder
@receiver(pre_save, sender=Mentor)
@receiver(pre_save, sender=Mentee)
@receiver(pre_save, sender=Training)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).docfile
    except sender.DoesNotExist:
        return False
    new_file = instance.docfile
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
