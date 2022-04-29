from distutils.command.upload import upload
from hashlib import blake2b
import imp
from re import template
from unicodedata import name
from xml.dom import UserDataHandler
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from django import forms


# Create your models here.
class Conference(models.Model):
    name = models.CharField(max_length=500)
    acronym = models.CharField(max_length=500)
    webpage = models.CharField(max_length=500)
    city = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    startdate = models.DateField()
    registrationdeadline = models.DateField()
    soumissiondeadline = models.DateField()
    primaryresearch = models.CharField(max_length=500)
    secoundaryresearch = models.CharField(max_length=500)
    areanite = models.CharField(max_length=500)
    topicone = models.CharField(max_length=500)
    topictwo = models.CharField(max_length=500)
    topicthree = models.CharField(max_length=500)
    topicfour = models.CharField(max_length=500)
    pdftem = models.FileField(upload_to='documents/',default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
