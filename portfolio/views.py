from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Project

def homepage(request):
    project = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects':project})
