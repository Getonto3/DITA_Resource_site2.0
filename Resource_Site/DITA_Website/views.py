from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

# Create your views here.
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