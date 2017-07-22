# -*- coding: utf-8 -*-
import os
from django.db import models

class Document(models.Model):

    Filename = models.CharField(max_length=25, blank=True)

    Week_1 = 'Week_1'
    Week_2 = 'Week_2'
    Week_3 = 'Week_3'
    Week_4 = 'Week_4'
    Mentee = 'Mentee'
    Mentor = 'Mentee'
    Training = 'Training'

    Weekly_Choices = (
        (Week_1, 'Week_1'),
        (Week_2, 'Week_2'),
        (Week_2, 'Week_3'),
        (Week_2, 'Week_4')
    )

    Role_Choices = (
        (Mentee, 'Mentee'),
        (Mentor, 'Mentor'),
        (Training, 'Training')
    )

    Role = models.CharField(max_length=25, choices=Role_Choices, default=Mentee, blank=False)
    Week = models.CharField(max_length=10, choices=Weekly_Choices, default=Week_1, blank=False)

    def choices_location(instance, filename):
        if instance.Week == 'Week_1' and instance.Role == 'Mentee':
            return os.path.join('documents', 'Week_1', 'Mentee', filename)
        elif instance.Week == 'Week_2' and instance.Role == 'Mentee':
            return os.path.join('documents', 'Week_2', 'Mentee', filename)
        elif instance.Week == 'Week_3' and instance.Role == 'Mentee':
            return os.path.join('documents', 'Week_3', 'Mentee', filename)
        elif instance.Week == 'Week_4' and instance.Role == 'Mentee':
            return os.path.join('documents', 'Week_4', 'Mentee', filename)
        elif instance.Week == 'Week_1' and instance.Role == 'Mentor':
            return os.path.join('documents', 'Week_1', 'Mentor', filename)
        elif instance.Week == 'Week_2' and instance.Role == 'Mentor':
            return os.path.join('documents', 'Week_2', 'Mentor', filename)
        elif instance.Week == 'Week_3' and instance.Role == 'Mentor':
            return os.path.join('documents', 'Week_3', 'Mentor', filename)
        elif instance.Week == 'Week_4' and instance.Role == 'Mentor':
            return os.path.join('documents', 'Week_4', 'Mentor', filename)
        elif instance.Week == 'Week_1' and instance.Role == 'Training':
            return os.path.join('documents', 'Week_1', 'Training', filename)
        elif instance.Week == 'Week_2' and instance.Role == 'Training':
            return os.path.join('documents', 'Week_2', 'Training', filename)
        elif instance.Week == 'Week_3' and instance.Role == 'Training':
            return os.path.join('documents', 'Week_3', 'Training', filename)
        elif instance.Week == 'Week_4' and instance.Role == 'Training':
            return os.path.join('documents', 'Week_4', 'Training', filename)
        else :
            return os.path.join(filename)

    docfile = models.FileField(upload_to=choices_location)
