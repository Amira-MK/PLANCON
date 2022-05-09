from ast import Delete
from distutils.command.upload import upload
from hashlib import blake2b
import imp
from re import template
from tkinter import CASCADE
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

    
class Chaiman (User):
    conf = models.ForeignKey(Conference,on_delete=models.CASCADE)
    
class Author(models.Model):
    first_name = models.CharField(max_length=50)  
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    country = models.CharField(max_length=25)
    organization = models.CharField(max_length=255)
    webpage = models.CharField(max_length=55)  

class Article(models.Model):
    title = models.CharField(max_length=100)
    abstract = models.TextField(max_length=1000)
    domaine = models.CharField(max_length=100)
    sous_domaine = models.CharField(max_length=100)
    keywords = models.TextField(max_length=100)
    file = models.FileField()
    aurhor=models.OneToOneField(Author, on_delete=models.CASCADE, null=True)

class association(models.Model):
    articleid = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    Confid = models.ForeignKey(Conference, on_delete=models.CASCADE, null=True)