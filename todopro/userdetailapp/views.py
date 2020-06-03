from django.shortcuts import render
from . models import Project

# Create your views here.

def project(request):
    projects = Project.objects.all()
    return render(request,'todoapp/home.html',{'projects':projects})
