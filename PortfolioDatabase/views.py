from django.shortcuts import render
from django.http import HttpResponse
from .models import Hobby, Project
from django.template import loader

# Create your views here.
def home(request):
    return render(request, 'PortfolioDatabase/index.html')

def hobbies(request):
    return render(request, 'PortfolioDatabase/listview.html', {'item_list': Hobby.objects.all()})

def portfolio(request):
    return render(request, 'PortfolioDatabase/listview.html', {'item_list': Project.objects.all()})

def contact(request):
    return render(request, 'PortfolioDatabase/contact.html')

def hobby_detail(request, hobby_id):
    return render(request, 'PortfolioDatabase/detail.html', {'item': Hobby.objects.get(id=hobby_id)})

def project_detail(request, project_id):
    return render(request, 'PortfolioDatabase/detail.html', {'item': Project.objects.get(id=project_id)})