
from cProfile import Profile
from multiprocessing import context
from re import template
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from .forms import Conferenceform
from .models import Conference
from django.core.files.storage import FileSystemStorage

# Create your views here.


def index(request):
    return render(request, 'dashboard/index.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def addcon(request):
    allconf= Conference.objects.all()
    subbmitted = False
    if request.method=="POST":
        form = Conferenceform(request.POST , request.FILES)
        if form.is_valid():
            fs=form.save(commit=False)
            fs.user=request.user
            fs.save()
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