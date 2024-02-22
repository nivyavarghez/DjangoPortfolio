from django.shortcuts import render
from projects.models import Project

# Create your views here (start from Leverage the Django Admin Site 17-02-2024).
def project_index(request):
    projects = Project.objects.all()
    context={
        "projects": projects
    }
    return render(request,"projects/project_index.html",context)

def project_detail(request, pk):
    project = Project.objects.get(pk =pk)
    context ={
        "project" : project
    }
    return render(request, "projects/project_detail.html",context)

