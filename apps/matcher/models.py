# -*- coding: utf-8 -*-
import uuid
from django.db import models


class Helper(models.Model):
    SKILL_LEVEL_CHOICES = [
        ('1', 'BASIC'),
        ('2', 'INTERMEDIATE'),
        ('3', 'APPROBATION'),
        ('4', 'EXPERT')
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    e_mail = models.CharField(max_length=200)
    phone_nbr = models.CharField(max_length=25)
    skill_level = models.CharField(
        max_length=1,
        choices=SKILL_LEVEL_CHOICES,
        default='1',  # BASIC
    )
    post_code = models.CharField(max_length=25)
    radius = models.IntegerField(default=50)
    validated = models.BooleanField(default=False)

    def __str__(self):  # Python 3: def __unicode__(self):
        return f'{self.first_name} {self.last_name} {self.post_code}'


class Hospital(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    e_mail = models.CharField(max_length=200)
    phone_nbr = models.CharField(max_length=25)
    first_name_contact = models.CharField(max_length=200)
    last_name_contact = models.CharField(max_length=200)
    post_code = models.CharField(max_length=25)
    street = models.CharField(max_length=200)
    validated = models.BooleanField(default=False)

    def __str__(self):  # Python 3: def __unicode__(self):
        return self.name


class Inquiry(models.Model):
    SKILL_LEVEL_CHOICES = [
        ('1', 'BASIC'),
        ('2', 'INTERMEDIATE'),
        ('3', 'APPROBATION'),
        ('4', 'EXPERT')
    ]

    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    number_of_helpers = models.IntegerField()
    skill_level = models.CharField(
        max_length=1,
        choices=SKILL_LEVEL_CHOICES,
        default='1',  # BASIC
    )
