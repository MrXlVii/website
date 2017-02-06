# Create your views here. # howdy/views.py

from django.shortcuts import render
from django.views import generic
from .models import Project


# Create your views here.
class HomePageView(generic.TemplateView):
    template_name = "index.html"

class AboutPageView(generic.TemplateView):
    template_name = "about.html"

class EssaysPageView(generic.TemplateView):
    template_name = "essays.html"

class ProjectsListView(generic.ListView):
    model = Project
    template_name = "projects.html"
        
