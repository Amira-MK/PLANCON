from dataclasses import fields
from importlib.metadata import files
from pyexpat import model
from re import template
from secrets import choice
from statistics import mode
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from .models import Article, Author, Conference, Reviewer, affectation, reviewing, aboutrev


class DateInput(forms.DateInput):
    input_type = 'date' 


class Conferenceform(ModelForm):
    name = forms.CharField(max_length=500)
    acronym = forms.CharField(max_length=500)
    webpage = forms.CharField(max_length=500)
    city = forms.CharField(max_length=500)
    country = forms.CharField(max_length=500)
    startdate = forms.DateField(widget=DateInput)
    registrationdeadline = forms.DateField(widget=DateInput)
    soumissiondeadline = forms.DateField(widget=DateInput)
    primaryresearch = forms.CharField(max_length=500)
    secoundaryresearch = forms.CharField(max_length=500)
    areanite = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":64}))
    topicone = forms.CharField(max_length=500)
    topictwo = forms.CharField(max_length=500)
    topicthree = forms.CharField(max_length=500)
    topicfour = forms.CharField(max_length=500)
    pdftem = forms.FileField()
    reviewerOne = forms.ModelChoiceField(queryset=User.objects.all())#!except current user
    reviewerTwo = forms.ModelChoiceField(queryset=User.objects.all())
    reviewerThree = forms.ModelChoiceField(queryset=User.objects.all())
    class Meta:
        model = Conference
        fields = ('name','acronym','webpage','city','country','startdate','registrationdeadline','soumissiondeadline','primaryresearch','secoundaryresearch','areanite','topicone','topictwo','topicthree','topicfour','pdftem','reviewerOne', 'reviewerTwo', 'reviewerThree')



class Articleform(ModelForm):
    title = forms.CharField(max_length=100)
    abstract = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":64}))
    domaine = forms.CharField(max_length=100)
    sous_domaine = forms.CharField(max_length=100)
    keywords = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":64}))
    file = forms.FileField()
    class Meta:
        model = Article
        fields = ('title','abstract','domaine','sous_domaine','keywords','file')

class Authorform(ModelForm):
    first_name = forms.CharField(max_length=50)  
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    country = forms.CharField(max_length=25)
    organization = forms.CharField(max_length=255)
    webpage = forms.CharField(max_length=55)  
    class Meta:
        model = Author
        fields = ('first_name','last_name','email','country','organization','webpage')


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length= 50)
    last_name = forms.CharField(max_length= 50)
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1','password2')


#class AffecterForm(ModelForm):
 #   reviewerOne = forms.ModelChoiceField(queryset=User.objects.all())
  #  class Meta:
   #     model = affecter
    #    fileds = ('reviewerOne')

class affecterReviewerForm(ModelForm):
    reviewer = forms.ModelChoiceField(queryset=Reviewer.objects.all()) #Todo : imported from conference  not from Reviewer 
    class Meta:
        model = affectation
        fields = ('reviewer',)

class aboutrevForm(ModelForm):
    CHOICES = (
        ('You have been selected!!!', 'You have been selected'),
        ('You are not selected!!!', 'You are not selected '),
    )
    observationn = forms.CharField(max_length=500 ,widget=forms.Select(choices=CHOICES))
    class Meta:
        model = aboutrev
        fields = ('observationn',)

class reviewingform(ModelForm):
    globalorig = forms.CharField(max_length=500)
    originality = forms.CharField(max_length=500)
    soundness = forms.CharField(max_length=500)
    presentation = forms.CharField(max_length=500)
    relevence = forms.CharField(max_length=500)
    importance = forms.CharField(max_length=500)
    observation = forms.CharField(max_length=500)
    CHOICES = (
        ('STRONG ACCEPT!', 'Strong Accept'),
        ('ACCEPT', 'Accept'),
        ('BORDERLINE', 'Borderline'),
        ('WEAK', 'Weak'),
        ('REJECT', 'Reject'),
    )
    finall = forms.CharField(max_length=500 , widget=forms.Select(choices=CHOICES))
   
    class Meta:
        model = reviewing
        fields = ('globalorig','originality','soundness','presentation','relevence','importance','observation','finall')