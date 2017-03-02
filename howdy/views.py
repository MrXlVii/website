# Create your views here. # howdy/views.py

from django.shortcuts import render, render_to_response, get_object_or_404
from django.views import generic
from .models import Project, Post, Category
from django.utils import timezone

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
'''
def essays(request):
    return render_to_response('essays.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })  
'''
def project_list(request):
    projects = Project.objects.order_by('last_update')
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'howdy/project_detail.html', {'project': project})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'howdy/post_detail.html', {'post': post})

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': Post.objects.filter(category=category)[:5]
    })

