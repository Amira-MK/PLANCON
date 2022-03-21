from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

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
            return redirect ('/dashboard/')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form' : form})


#idk why is it working but dont touch it
def post(request):
    return render(request, 'dashboard/post.html')
    
def logout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,('you logged out!'))
        return render(request, 'logout')