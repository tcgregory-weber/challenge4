from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Hobby, Project
from django.template import loader
from .forms import ContactForm, PortfolioForm

# Create your views here.
def home(request):
    return render(request, 'PortfolioDatabase/index.html')

def hobbies(request):
    return render(request, 'PortfolioDatabase/listview.html', {'item_list': Hobby.objects.all()})

def portfolio(request):
    return render(request, 'PortfolioDatabase/listview.html', {'item_list': Project.objects.all()})

def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('port_db:home')

    return render(request, 'PortfolioDatabase/contact.html', {'form': form})

def hobby_detail(request, hobby_id):
    return render(request, 'PortfolioDatabase/detail.html', {'item': Hobby.objects.get(id=hobby_id)})

def project_detail(request, project_id):
    return render(request, 'PortfolioDatabase/detail.html', {'item': Project.objects.get(id=project_id)})

def addProject(request):
    form = PortfolioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('port_db:portfolio')

    return render(request, 'PortfolioDatabase/addProject.html', {'form': form})

def updateProject(request, project_id):
    project = Project.objects.get(id=project_id)
    form = PortfolioForm(request.POST or None, instance=project)

    if form.is_valid():
        form.save()
        return redirect('port_db:portfolio')

    return render(request, 'PortfolioDatabase/addProject.html', {'form': form, 'project': project})

def deleteProject(request, project_id):
    project = Project.objects.get(id=project_id)

    if request.method == 'POST':
        project.delete()
        return redirect('port_db:portfolio')

    return render(request, 'PortfolioDatabase/deleteProject.html', {'project': project})