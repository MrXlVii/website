# Create your views here. # howdy/views.py

from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.views import generic
from .models import Post, Category
from django.utils import timezone
from .forms import PostForm

# Create your views here.
class HomePageView(generic.TemplateView):
    template_name = "index.html"

class ContactPageView(generic.TemplateView):
    template_name = "contact.html"

"""
class ProjectListView(generic.ListView):
    model = Project


class ProjectDetailView(generic.DetailView):
    model = Project
"""

def essays(request):
    return render_to_response('essays.html', {
        'categories': Category.objects.all(),
        'posts': Post.objects.all()[:5]
    })  

"""
def project_list(request):
    projects = ProjectNew.objects.order_by('last_update')
    return render(request, 'project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'howdy/project_detail.html', {'project': project})
"""
def post_list(request):
    posts = Post.objects.filter(posted_date__lte=timezone.now()).order_by('posted_date')
    return render(request, 'howdy/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'howdy/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.posted_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'howdy/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.posted_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'howdy/post_edit.html', {'form': form})

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

