# Create your views here. # howdy/views.py

from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import generic
from .models import Project, Blog, Category

# Create your views here.
class HomePageView(generic.TemplateView):
    template_name = "index.html"


class EssaysPageView(generic.TemplateView):
    template_name = "essays.html"


class ContactPageView(generic.TemplateView):
    template_name = "contact.html"


class ProjectListView(generic.ListView):
    model = Project


class ProjectDetailView(generic.DetailView):
    model = Project

def essays(request):
    return render_to_response('essays.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.all()[:5]
    })

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })
