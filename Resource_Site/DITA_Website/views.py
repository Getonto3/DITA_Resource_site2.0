from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import login, authenticate,logout
from .forms import SignUpForm, LoginForm


def Homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def Hardware(request):
    template = loader.get_template('hardware.html')
    return HttpResponse(template.render())

def Software(request):
    template = loader.get_template('software.html')
    return HttpResponse(template.render())

def Tutor(request):
    template = loader.get_template('tutor.html')
    return HttpResponse(template.render())
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage') 
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage') 
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('homepage')