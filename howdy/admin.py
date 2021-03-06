from django.contrib import admin
from django import forms
from .models import Language, Post, Category, Project

# Register your models here.

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title',)

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    form = PostForm


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = ProjectForm
    

admin.site.register(Language)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Project)
