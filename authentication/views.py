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
from platformdirs import user_cache_dir
from .forms import  RegisterForm, affecterReviewerForm
from .forms import affecterReviewerForm ,Conferenceform, Articleform, Authorform
from .models import Chairman, Conference, Reviewer, affectation
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound
import os
from .models import Article
from .models import Author
from . import models
from django.http import FileResponse

# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')

def dashboard(request):
    conferences = Conference.objects.all()
    notmyconferences = []
    for conference in conferences:
        if conference.user != request.user:
            notmyconferences.append(conference)
    #Conferences = Conference.objects.all()
    return render(request, 'dashboard/dashboard.html',{'notmyconferences':notmyconferences})

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
          conf = Conference.objects.get(pk=conf_id)
          conf.article.add(fs)
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

def myConferences(request):
    conferences = Conference.objects.all()
    myconferences = []
    for conference in conferences:
        if conference.user == request.user:
            myconferences.append(conference)
    return render(request, 'dashboard/myconfe.html', {'myconferences': myconferences})

def myview(request ):
    conferences = Conference.objects.all()
    myconferences = []
    for conference in conferences:
        if conference.reviewerOne == request.user or  conference.reviewerTwo == request.user or  conference.reviewerThree == request.user:
            myconferences.append(conference)
    return render(request, 'dashboard/myview.html',{'myconferences': myconferences})


def about_myconf(request ,conf_id):
    myconference = Conference.objects.get(pk=conf_id)
    return render(request, 'dashboard/about_myconf.html',{'Conference':myconference})

def about_myconfmyrev(request ,conf_id):
    myconference = Conference.objects.get(pk=conf_id)
    return render(request, 'dashboard/about_myconfmyrev.html',{'Conference':myconference})

def submitedArticles(request,conf_id):
    articles = Conference.objects.get(pk=conf_id).article.all()
    conference = Conference.objects.get(id=conf_id)
    return render(request, 'dashboard/submittedArticle.html', {'articles': articles,'conference':conference})

def Articlesrev(request,conf_id):
    # conference = Conference.objects.get(id=conf_id)
    # reviewer=Reviewer(user=request.user,conference=conference)
    # articles = affectation.objects.get(reviewer).article.all()
    # #art = affectation.objects.get(pk=affectation_id).article.all()
    # myarticles = []
    # for article in articles: 
    #     myarticles.append(article.article)
    affs = affectation.objects.all()
    conference = Conference.objects.get(id=conf_id)
    myarticles = []
    for articlee in affs:
        if articlee.reviewer.user == request.user and articlee.conferencee == conference:
            myarticles.append(articlee.article)
        print(myarticles)
    return render(request, 'dashboard/Articlesrev.html', {'myarticles': myarticles,'conference':conference})

def aboutArticle(request,article_id, conf_id):
    conference = Conference.objects.get(id=conf_id)
    article = Article.objects.get(pk=article_id)
    form = affecterReviewerForm(request.POST)

    if request.method == "POST" :
        if form.is_valid():
            fs=form.save(commit=False)
            fs.user=request.user
            reviewer=Reviewer.objects.get(user=fs.reviewer.user) and Reviewer.objects.get(conference=conference)
            # if reviewer.user != fs.reviewer.user:
            #     reviewer=Reviewer(user=fs.reviewer.user,conference=conference)
            #     reviewer.save()
            aff = affectation(conferencee=conference,article=article, reviewer = reviewer)
            aff.save()
        else:
            form = affecterReviewerForm
    return render(request, 'dashboard/aboutArticle.html',{'form':form,'article':article, 'conference':conference})

def aboutArticlee(request,article_id, conf_id):
    conference = Conference.objects.get(id=conf_id)
    article = Article.objects.get(pk=article_id)
    form = affecterReviewerForm(request.POST)

    if request.method == "POST" :
        if form.is_valid():
            fs=form.save(commit=False)
            fs.user=request.user
            reviewer=Reviewer.objects.get(user=fs.reviewer.user) and Reviewer.objects.get(conference=conference)
            # if reviewer.user != fs.reviewer.user:
            #     reviewer=Reviewer(user=fs.reviewer.user,conference=conference)
            #     reviewer.save()
            aff = affectation(conferencee=conference,article=article, reviewer = reviewer)
            aff.save()
        else:
            form = affecterReviewerForm
    return render(request, 'dashboard/aboutArticlee.html',{'form':form,'article':article, 'conference':conference})


def submitedArticles(request,conf_id):
    articles = Conference.objects.get(pk=conf_id).article.all()
    conference = Conference.objects.get(id=conf_id)
    return render(request, 'dashboard/submittedArticle.html', {'articles': articles,'conference':conference})




def update_myconf(request, conf_id):
    myconference = Conference.objects.get(pk=conf_id)
    form = Conferenceform(request.POST or None, instance=myconference)
    if form.is_valid():
        form.save()
        return redirect('plancon:myConferences')
    return render(request, 'dashboard/updateConf.html',{'Conference':myconference, 'form':form})


def delete_myconf(request, conf_id):
    myconference = Conference.objects.get(pk=conf_id)
    myconference.delete()
    return redirect('plancon:myConferences')