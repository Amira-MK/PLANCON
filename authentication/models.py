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

class Article(models.Model):
    title = models.CharField(max_length=100)
    abstract = models.TextField(max_length=1000)
    domaine = models.CharField(max_length=100)
    sous_domaine = models.CharField(max_length=100)
    keywords = models.TextField(max_length=100)
    file = models.FileField()
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    
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
    article=models.ManyToManyField(Article,related_name='conferences',blank = True)
    reviewerOne = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='reviewerOne')
    reviewerTwo = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='reviewerTwo')
    reviewerThree = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='reviewerThree')




class Chairman(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #reveiwers = models.ManyToManyField(User, related_name='reviewers', blank=True)
    conference = models.OneToOneField(Conference, related_name='conference', on_delete=models.CASCADE, blank=False, null=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 


    def get_reveiwers(self):
        return self.reveiwers.all() 

    def get_reviewers_count(self):
        return self.reveiwers.count()

    class Meta:
        verbose_name_plural = "Chairmen"


    def __str__(self):
        return str(self.user)
class Author(models.Model):
    first_name = models.CharField(max_length=50)  
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    country = models.CharField(max_length=25)
    organization = models.CharField(max_length=255)
    webpage = models.CharField(max_length=55)  
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Reviewer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)  

    def __str__(self):
        return str(self.user)


class affectation(models.Model):
    conferencee = models.ForeignKey(Conference,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer,on_delete=models.CASCADE)



class reviewing(models.Model):
    globalorig = models.CharField(max_length=500)
    originality= models.CharField(max_length=500)
    soundness = models.CharField(max_length=500)
    presentation = models.CharField(max_length=500)
    relevence = models.CharField(max_length=500)
    importance = models.CharField(max_length=500)
    observation = models.CharField(max_length=500)
    conferencee = models.ForeignKey(Conference,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    CHOICES = (
        ('STRONG ACCEPT!', 'Strong Accept'),
        ('ACCEPT', 'Accept'),
        ('BORDERLINE', 'Borderline'),
        ('WEAK', 'Weak'),
        ('REJECT', 'Reject'),
    )
    finall= models.CharField(max_length=500 , choices = CHOICES)
    #reviewed = models.BooleanField( default=False)
    
class aboutrev(models.Model):
    conferencee = models.ForeignKey(Conference,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    reviewingg = models.ForeignKey(reviewing,on_delete=models.CASCADE)
    CHOICES = (
        ('You have been selected!!!', 'You have been selected'),
        ('You are not selected!!!', 'You are not selected '),
    )
    observationn = models.CharField(max_length=500,choices = CHOICES)