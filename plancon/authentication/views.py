
from cProfile import Profile
from multiprocessing import context
from re import template
from urllib.request import Request
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import is_valid_path
from .forms import RegisterForm
from .forms import Conferenceform, Articleform, Authorform
from .models import Chairman, Conference, Reviewer
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
import os
from .models import Article
from .models import Author
from django.http import FileResponse

# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')

def dashboard(request):
    Conferences = Conference.objects.all()
    return render(request, 'dashboard/dashboard.html',{'Conferences':Conferences})

def aboutconf(request ,conf_id):
    myconference = Conference.objects.get(pk=conf_id)
    filepath = os.path.join('static', 'sample.pdf')
    return render(request, 'dashboard/aboutconf.html',{'Conference':myconference})

def addarticle(request,conf_id):
    myconference = Conference.objects.get(pk=conf_id)
    allarticle = Article.objects.all()
    researcher = Author.objects.all()
    if request.method == 'POST':
       form = Articleform(request.POST , request.FILES)
       form1 = Authorform (request.POST)
       if form.is_valid() and form1.is_valid():
          fs=form.save(commit=False)
          fs.user=request.user
          fs.save()
          fa=form1.save(commit=False)
          fa.user=request.user
          fa.save()

       else:
            form = Articleform
            form1 = Authorform
    form = Articleform
    form1 = Authorform
    context={'form':form,'form1':form1,'allarticle':allarticle,'researcher':researcher,'Conference':myconference,}
    return render (request, 'dashboard/addarticle.html',context)



def addcon(request):
    allconf= Conference.objects.all()
    subbmitted = False
    if request.method=="POST":
        form = Conferenceform(request.POST , request.FILES)
        if form.is_valid():
            fs=form.save(commit=False)
            fs.user=request.user
            fs.save()
           
            
            chairman = Chairman(user=request.user, conference=fs)
            chairman.save()

            reviewer = Reviewer(user=fs.reviewerOne, conference=fs)
            reviewer.save()
            reviewer = Reviewer(user=fs.reviewerTwo, conference=fs)
            reviewer.save()
            reviewer = Reviewer(user=fs.reviewerThree, conference=fs)
            reviewer.save()

            return redirect("plancon:addcon")
        else:
            form = Conferenceform
            if 'subbmitted' in request.GET:
                subbmitted = True 
        
    form = Conferenceform
    context={'form':form,'allconf':allconf,'subbmitted':subbmitted,}
    return render(request, 'dashboard/addcon.html',context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            #log user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate( username = username, password = password )
            login(request, user)
            messages.success(request,('you created an account'))
            return redirect ('/dashboard')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form' : form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            messages.success(request,('you logged in!'))
            return redirect('plancon:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

#idk why is it working but dont touch it
def post(request):
    return render(request, 'dashboard/post.html')
    
def logout_view(request):
    logout(request)
    messages.success(request,('you logged out!'))
    return redirect('plancon:index')