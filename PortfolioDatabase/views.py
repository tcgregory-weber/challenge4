from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby, Project

# Create your views here.
def home(request):
    return HttpResponse("Hello, world! " + 
        "My name is Tyler Gregory, and I am a senior here at WSU.")

def hobbies(request):
    hobbies = Hobby.objects.all()
    return HttpResponse(hobbies)

def portfolio(request):
    projects = Project.objects.all()
    return HttpResponse(projects)

def contact(request):
    return HttpResponse("tylergregory1@mail.weber.edu")