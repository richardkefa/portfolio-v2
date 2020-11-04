from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Projects
# Create your views here.
def welcome(request):
  projects = Projects.get_projects()
  return render(request,"all-projects/projects", {"projects":projects})