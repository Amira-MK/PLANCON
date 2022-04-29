from dataclasses import fields
from pyexpat import model
from re import template
from statistics import mode
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Conference


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
    class Meta:
        model = Conference
        fields = ('name','acronym','webpage','city','country','startdate','registrationdeadline','soumissiondeadline','primaryresearch','secoundaryresearch','areanite','topicone','topictwo','topicthree','topicfour','pdftem')



class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length= 50)
    last_name = forms.CharField(max_length= 50)
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1','password2')

