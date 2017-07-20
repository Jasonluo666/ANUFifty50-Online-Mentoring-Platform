# -*- coding: utf-8 -*-
from django.db import models
from djchoices import DjangoChoices, ChoiceItem
import os, sys
#class Week(models.Model):

#    week = models.IntegerField()
#    semester = models.CharField(max_length=16)
'''
class Week_Choices(DjangoChoices):
    Week_1 = ChoiceItem(1, 'Week1')
    Week_2 = ChoiceItem(2, 'Week2')
    Week_3 = ChoiceItem(3, 'Week3')
    Week_4 = ChoiceItem(4, 'Week4')

class Role_Choices(DjangoChoices):
    Mentee = ChoiceItem(1, 'Mentee')
    Mentor = ChoiceItem(2, 'Mentor')
    Training = ChoiceItem(3, 'Training')
'''
def location(instance, filename):
    '''
    if instance.Weekly_Choices == 'Week1':
        return 'documents/'+ Week1 + '/' + 'Mentee' + filename
    elif instance.Weekly_Choices == 'Week2':
        return 'documents/'+ Week2 + '/' + 'Mentee' + filename
    elif instance.Weekly_Choices == 'Week3':
        return 'documents/'+ Week3 + '/' + 'Mentee' + filename
    elif instance.Weekly_Choices == 'Week4':
        return 'documents/'+ Week4 + '/' + 'Mentee' + filename
    '''
    if instance.Week == 'Week1':
        return 'documents/' + Week_1 + '/' + 'Mentee' + filename
    elif instance.Week == 'Week2':
        return 'documents/' + Week_2 + '/' + 'Mentee' + filename
    elif instance.Week == 'Week3':
        return 'documents/' + Week_3 + '/' + 'Mentee' + filename
    elif instance.Week == 'Week4':
        return 'documents/' + Week_4 + '/' + 'Mentee' + filename
"""
def location(instance, filename):
    if Week_Choices.choices == 'Week1':
        return os.path.join('documents', 'Week_1', 'Mentee', filename)
    elif Week_Choices.choices == 'Week2':
        return os.path.join('documents', 'Week_2', 'Mentee', filename)
    elif Week_Choices.choices == 'Week3':
        return os.path.join('documents', 'Week_3', 'Mentee', filename)
    elif Week_Choices.choices == 'Week4':
        return os.path.join('documents', 'Week_4', 'Mentee', filename)
    else:
        return os.path.join('documents', filename)
"""

class Document(models.Model):
    #week = models.ForeignKey('Week', ) # app name in ###, also is this optional?
    Name = models.CharField(max_length=25, blank=True)
    Week_1 = 'Week1'
    Week_2 = 'Week2'
    Week_3 = 'Week3'
    Week_4 = 'Week4'
    Mentee = 'Mentee'
    Mentor = 'Mentee'
    Training = 'Training'

    Weekly_Choices = (
        (Week_1, 'Week_1'),
        (Week_2, 'Week_2'),
        (Week_3, 'Week_3'),
        (Week_4, 'Week_4')
    )

    Role_Choices = (
        (Mentee, 'Mentee'),
        (Mentor, 'Mentor'),
        (Training, 'Training')
    )

    Mentee_Mentor = models.CharField(max_length=25, choices=Role_Choices, default=Mentee, blank=False)
    Week = models.CharField(max_length=10, choices=Weekly_Choices, default=Week_1, blank=False)
    #docfile = models.FileField(upload_to='documents/'+ 'mentee' + '/' + 'Mentee') # path may be malformed"""
    docfile = models.FileField(upload_to=location)


#class Document(models.Model):
    #docfile = models.FileField()
    #docfile = models.FileField(upload_to='documents/%Y/%m/%d')
    """name = models.CharField(max_length=25, blank=True)
    Week_1 = 'W1'
    Week_2 = 'W2'
    Week_3 = 'W3'
    Week_4 = 'W4'
    Weekly_Content_CHOICES = (
        (Week_1, 'Week1'),
        (Week_2, 'Week2'),
        (Week_3, 'Week3'),
        (Week_4, 'Week4'),
    )
    Folder = models.CharField(
        max_length=2,
        choices=Weekly_Content_CHOICES,
        default=Week_1,
    )
    if Weekly_Content_CHOICES == 'Week1'
        docfile.upload_to = 'documents/Week1/'
    elif Weekly_Content_CHOICES == 'Week2'
        docfile.upload_to = 'documents/Week2/'
    elif Weekly_Content_CHOICES == 'Week3'
        docfile.upload_to = 'documents/Week3/'
    else
        docfile.upload_to = 'documents/Week4/'"""
